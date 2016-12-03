
import time
import os
import picamera

import paramiko
import scp

import threading

from serial_com import temp_view, temp_set

class SSH_Thread(Thread):
        def __init__(self):
                Thread.__init__(self)

                self.start()
        def createSSHClient(server, port, user, password):
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(server, port, user, password)
            return client


        def run(self)

                ssh = createSSHClient('192.168.1.37', 22, 'sshd', 'Toshiba12')
                putter = scp.SCPClient(ssh.get_transport())

                putter.put(directory_str, directory_strREMOTE)


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

def reheat():
    curr_t = temp_view()
    x2 = abs(curr_t-20)/6
    linear_temp(x2,curr_t,20)


def linear_temp_shoot(x2, y1, y2, instantiation, duration):
#x2 == duration(in minutes)
#y1 == start temp
#y2 == finish temp
	
	"""convert all our minute values to seconds"""
	x2 = x2*60
	duration = duration*60

	m = ((y2-y1)/x2) #calculate slope

	camera = picamera.PiCamera()
	camera.resolution = (1024, 768)

	folder_make()

	n = 0 #this will incerment our time(seconds)
	photo_n = 1 #increment our photos 
	while n != x2:
		print n

		
		
		if n%instantiation == 0:
			lot = str(photo_n)
			time_val = time.strftime("%Y-%m-%d;%H:%M:%S")
			file_name = str(folder_name+'/'+lot+'~'+temp_view()+';'+time_val+'.jpg')
			camera.capture(file_name)
			photo_n+=1


		# x1 = 0 always, doesn't need to be included
		y = (m*n)+y1 #temp at given time(x)
		temp_set(y)
		n += 1
		time.sleep(1)

	if duration>x2:
		after = duration - x2
		while after >= duration:
			lot = str(photo_n)
			time_val = time.strftime("%Y-%m-%d;%H:%M:%S")
			file_name = str(folder_name+'/'+lot+'~'+temp_view()+';'+time_val+'.jpg')
			camera.capture()
			time.sleep(instantiation)
			after+=instantiation

	reheat()



linear_temp(1, 10.0, 5.0, 2, 1)


