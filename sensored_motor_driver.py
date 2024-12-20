from motor_driver import MotorDriver
from machine import Pin

class SensoredMotorDriver(MotorDriver):
    
    def __init__(self, drive_pin_ids, encoder_pin_ids, ab=1):
        # Pin configuration
        super().__init__(*drive_pin_ids)  # call super class's "__init__"
        self.enca_pin = Pin(encoder_pin_ids[0], Pin.IN, Pin.PULL_UP)  # yellow  
        self.encb_pin = Pin(encoder_pin_ids[1], Pin.IN, Pin.PULL_UP)  # white
        self.enca_pin.irq(trigger=Pin.IRQ_RISING, handler=self.update_counts)
        # Variables
        self.counts = 0
        # Properties
        self.AB = ab  # encoder channel order, 1: A rise first, -1: B rise first
        self.PPR = 12  # pulses per revolution, PPR * 4 = CPR
        self.GEAR_RATIO = 46.85  # speed reduction rate, v_wheel = v_motor / GEAR_RATIO
        self.WHEEL_RADIUS = 65 / 2000  # diameter in mm -> radius in m  
    
    def update_counts(self, pin):
        if self.encb_pin.value() == self.enca_pin.value():  # A channel RISE later than B channel
            self.counts -= self.AB
        else:
            self.counts += self.AB
        
if __name__ == '__main__':
    from time import sleep
    from math import pi
    smd = SensoredMotorDriver((11, 12, 13), (6, 7), -1)
    prev_counts = 0

    # Following computation can be wrapped in a Timer callback
    for d in range(200):  # ramp up
        smd.forward(int(65025 / 200 * d))
        sleep(0.02)
        pulses_inc = smd.counts - prev_counts
        prev_counts = smd.counts
        revs_inc = pulses_inc / smd.PPR
        rads_inc = revs_inc * 2 * pi
        ang_vel_motor = rads_inc / 0.02  # motor angular velocity
        ang_vel_wheel = ang_vel_motor / smd.GEAR_RATIO  # wheel angular velocity
        print(f"wheel angular velocity: {ang_vel_wheel} rad/s")
        lin_vel = ang_vel_wheel * smd.WHEEL_RADIUS
        print(f"wheel linear velocity: {lin_vel} m/s")
        
    for d in reversed(range(200)):  # ramp down
        smd.forward(int(65025 / 200 * d))
        sleep(0.02)
        pulses_inc = smd.counts - prev_counts
        prev_counts = smd.counts
        revs_inc = pulses_inc / smd.PPR
        rads_inc = revs_inc * 2 * pi
        ang_vel_motor = rads_inc / 0.02  # motor angular velocity
        ang_vel_wheel = ang_vel_motor / smd.GEAR_RATIO  # wheel angular velocity
        print(f"wheel angular velocity: {ang_vel_wheel} rad/s")
        lin_vel = ang_vel_wheel * smd.WHEEL_RADIUS
        print(f"wheel linear velocity: {lin_vel} m/s")

    smd.stop()
    
