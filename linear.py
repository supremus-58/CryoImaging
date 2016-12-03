import time

from serial_com import temp_set





def linear_temp(x2, y1, y2):
#x2 == duration(in minutes)
#y1 == start temp
#y2 == finish temp
	x = 0 #this will iterate our time(seconds)
	
	x2 = x2*60

	m = ((y2-y1)/x2) #calculate slope
	#print m
	#print '\n'


	while x != x2:
		
		# x1 = 0 always, doesn't need to be included
		y = (m*x)+y1 #temp at given time(x)
		temp_set(y)
		x += 1
		time.sleep(1)
