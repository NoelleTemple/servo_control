import RPi.GPIO as GPIO
import time

class servo:
	description = ""
	boardpin = 0
	frequency = 0

	def __init__(self, description = "servo", boardpin = 0, frequency = 50):
		self.description=description
		self.boardpin=boardpin
		self.frequency=frequency

	def getinfo(self):
		print("{}: board pin is {} and frequency is {}").format(self.description, self.boardpin, self.frequency)

	def setup(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.boardpin, GPIO.OUT)
	
	def moveservo(self, strtDC):
		p=GPIO.PWM(self.boardpin, self.frequency)
		p.start(0)
		p.ChangeDutyCycle(strtDC)
		time.sleep(2)
		p.ChangeDutyCycle(strtDC-5)
		time.sleep(2)
		p.ChangeDutyCycle(strtDC+5)
		time.sleep(2)
		p.stop
		GPIO.cleanup()
