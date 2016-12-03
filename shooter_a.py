"""
this will set variable to current date/time
variable does not reset until time.strftime() is called again
"""
import time
import os
import picamera

from serial_com import temp_view

from compoundpi.client import CompoundPiClient


def time_str():
	
	timestr_name = str(time.strftime("%Y-%m-%d;%H:%M:%S"))
	return timestr_name
	

folder_name = time_str()

def folder_make():
	
	try:
		os.makedirs(folder_name)
	except OSError:
		if not os.path.isdir(folder_name):
			raise


def shooting(instantiation, duration):

	folder_make()

	duration = duration*60 #input is in minutes, *60 seconds
	instances = int(duration/instantiation)

	with picamera.PiCamera() as camera:
		camera.resolution = (1024, 768)

		n = 1
		while n <= instances + 1:

			lot = str(n)
			time_val = time.strftime("%Y-%m-%d;%H:%M:%S")
			file_name = str(folder_name+'/'+lot+'~'+temp_view()+';'+time_val+'.jpg')
			camera.capture(file_name)
			time.sleep(instantiation)
			n+=1


shooting(2, 1)


