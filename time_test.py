import picamera
import time
import datetime
from serial_com import temp_view, temp_set


camera = picamera.PiCamera()
camera.resolution = (1024, 768)

a = datetime.datetime.now()
b = datetime.datetime.now()
c = b-a
print c
print '\r'

a1 = datetime.datetime.now()
camera.capture('test.jpg')
b1 = datetime.datetime.now()
c1 = b1-a1

print "amount of time to take photo:"
print c1, 'microsecs'
print '\r'

time.sleep(1)

a2 = datetime.datetime.now()
temp_view()
b2 = datetime.datetime.now()
c2 = b2-a2

time.sleep(1)

print "amount of time to read temperature from TC:"
print c2, 'microsecs'
print '\r'

time.sleep(1)

a3 = datetime.datetime.now()
temp_set(10.0)
b3 = datetime.datetime.now()

c3 = b3-a3

print "amount of time to set output temperature of TC"
print c3, 'microsecs'
