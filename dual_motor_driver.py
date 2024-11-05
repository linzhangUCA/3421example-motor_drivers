from motor_driver import MotorDriver

class DualMotorDriver:

    def __init__(self, lmotor_ids, rmotor_ids):
        self.left_motor = MotorDriver(lmotor_ids[0], lmotor_ids[1], lmotor_ids[2])
        self.right_motor = MotorDriver(*rmotor_ids)  # use "*" to unpack items in list/tuple
        
    def forward(self, duty):
        self.left_motor.forward(duty)
        self.right_motor.forward(duty)
        
    def backward(self, duty):
        self.left_motor.backward(duty)
        self.right_motor.backward(duty)

    def spin_left(self, duty):
        self.left_motor.backward(duty)
        self.right_motor.forward(duty)
        
    def spin_right(self, duty):
        self.left_motor.forward(duty)
        self.right_motor.backward(duty)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        
if __name__ == '__main__':
    from time import sleep
    dmd = DualMotorDriver((11, 12, 13), (18, 19, 20))
    dmd.forward(40000)
    sleep(2)
    dmd.stop()
    sleep(0.25)
    dmd.backward(40000)
    sleep(2)
    dmd.stop()
    sleep(0.25)
    dmd.spin_left(40000)
    sleep(2)
    dmd.stop()
    sleep(0.25)
    dmd.spin_right(40000)
    sleep(2)
    dmd.stop()
    sleep(0.25)
    