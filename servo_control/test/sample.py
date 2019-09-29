#sample code

#This is the setup we are testing with the sample
from servocntl_pkg import servo

#initialize the servo motor with a description, the pin number on the board (not the GPIO number
#and the frequency at which the PWM signal should run (50Hz is average)
test=servo(description="testing control of Servo", boardpin = 35, frequency = 50)
#this will print out all the information that you have set
test.getinfo()
#this will setup the GPIO pin as a pwm output pin
test.setup()
#this will move the servo, starting with a duty cycle of 7.5%
test.moveservo(7.5)
