#!/usr/bin/env python3
'''
Usage is described in README.md
'''

import wpilib

class MyRobot(wpilib.SampleRobot):
    def robotInit(self):
        i = 0
        self.motors = []

        # inits all 10 motors in an array
        while (i < 10):
            self.motors.append(wpilib.Jaguar(i))
            i = i + 1

        self.stick = wpilib.Joystick(0) # initialize the joystick on port 0

    def operatorControl(self):
        while self.isOperatorControl() and self.isEnabled():
            # reset all motors
            for motor in self.motors:
                motor.set(0)

            i = 1
            self.buttons = []

            # makes an array of buttons currently pressed
            while (i < 10):
                if (self.stick.getRawButton(i) == True):
                    self.buttons.append(i)
                i = i + 1

            # loops over button array
            for pressedB in self.buttons:
                self.motors[pressedB].set(self.stick.getY())
                print("Running PWM output " + str(pressedB))

            wpilib.Timer.delay(0.005)  # wait 5ms to the next update

if __name__ == "__main__":
    wpilib.run(MyRobot)
