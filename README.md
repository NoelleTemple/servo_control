#SERVO CONTROL

If you have not cloned this repo yet:
```
cd ~
git clone https://github.com/NoelleTemple/noelle_digital_controls.git
cd noelle_digital_controls/servo_control
```
If you have cloned this repo:
```
cd ~/noelle_digital_controls/servo_control
```

To use the sample code, set up a servo motor connecting the control signal to pin 35, ground to pin 39, and Vcc to pin 17 (you can change the control signal to any GPIO pin, if you change the code, Vcc to any 3.3 V pin, or 5 V depending on the servo, and ground to any ground pin).

Raspberry Pi Pinout:
https://learn.sparkfun.com/tutorials/raspberry-gpio/gpio-pinout

![Raspberry Pi Pinout](https://github.com/NoelleTemple/noelle_digital_controls/blob/master/picture/RPi_Pinout.jpg)


Example Servo:
https://components101.com/servo-motor-basics-pinout-datasheet

![Servo Pinout](https://github.com/NoelleTemple/noelle_digital_controls/blob/master/picture/ServoPinout.png)

Make sure to install the package:
```
cd ~/noelle_digital_controls/servo_control
sudo pip install -e .
```
This will automatically find the setup.py file and install the package.

Navigate to Sample code:
```
cd ~/noelle_digital_controls/servo_control/test
```
Run Sample code:
```
python sample.py
```
Here, the servo is identified with a desciption, the pin number on the board (not the GPIO pin number, but that can be changed as well), and the frequency at which the control signal will opporate.  This is the line in sample.py that defines these items:
```
test=servo(description="testing control of Servo", boardpin = 35, frequency = 50)
```
The description of this item is "testing control of Servo.
The boardpin is 35.
The frequency of the control signal is 50 Hz.  This is for a pwm signal with a period of 20 ms (1/50 Hz = 0.02 s)

In this code, the servo will move to 3 different positions, changing based on the duty cycle of the control signal.  This is the code that shows the changing duty cycle.
```
p.ChangeDutyCycle(7.5)
time.sleep(2)
```
The duty cycle is directly related to the position of the servo motor.  The time off / total time is the duty cycle.  Different servo motors will vary based on their range. 

To find this code:
```
nano ~/noelle_digital_controls/servo_control/servocntl_pkg/servo.py
```
Here, the description of the servo, the pin number on the board, and the frequency at which the PWM signal operates is initialized.  Also included is a module to print that information, another to setup the pin for PWM output, and another that moves the motor based on the duty cycled entered:

```
test.moveservo(7.5)
```
This will move the servo to the center position, then 90 degrees to the right, and 180 degrees from there to the left.


servo.py utilizes the GPIO package, this comes pre-installed with Raspbian.  
This code was based off of information found at these two websites.  For more information on GPIO, visit:
```
https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
https://projects.raspberrypi.org/en/projects/grandpa-scarer/4
```
