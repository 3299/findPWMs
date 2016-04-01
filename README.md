# findPWMs
A simple tool to figure out which motor is connected to which PWM output.  If you're anything like us, you zip-tied all the PWM wires into a nice bundle; only realizing afterwards that you had no clue what motor was connected to what output.  Even if you're exceptionally neat with wiring, this can still be useful in testing and verifying that all motors work.

## Usage
You'll need a joystick that has at least 9 buttons, including the trigger.

1. Clone this repo
2. Upload robot.py to robot
3. Press button *n* (trigger is 1), and label the blinking motor controller accordingly (remember that the joystick buttons are labeled 1-9, but PWM slots are labeled 0-9) and move the Y-axis
4. Repeat 3 until all motor controllers have been labeled
