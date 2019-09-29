from setuptools import setuptools

setuptools.setup(
	name='Control_Servo',
	version='1.0.0',
	description='Control A Servo Motor Using GPIO',
	url='https://github.com/NoelleTemple/noelle_digital_controls/upload/master/servo_control',
	author='Noelle Lewandowski',
	packages=setuptools.find_packages(),
	install_requires=['RPi.GPIO']
)
