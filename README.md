# 3421example-motor_drivers
This repo contains Micropython examples of driving [geared DC motors](https://www.pololu.com/product/4805) using [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) and a [dual-channel DC motor driver](https://www.dfrobot.com/product-1861.html).

## Description
1. [motor_driver.py](motor_driver.py) drives a single motor using 3 Pico's GP pins.
2. [dual_motor_driver.py](dual_motor_driver.py) drives two motors using 6 Pico's GP pins.
3. [sensored_motor_driver.py](sensored_motor_driver.py) drives a single motor as well as read encoder's signals with 2 extra Pico's GP pins.
4. [sensored_dual_motor_driver.py](sensored_dual_motor_driver.py) drives two motors as well as read encoders' signals with 4 extra Pico's GP pins.
