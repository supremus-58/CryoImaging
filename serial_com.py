import serial


#identifying paramaters for serial comm
ser = serial.Serial('/dev/ttyUSB0', 230400, timeout=.5)


#ascii <*> initiates serial comm with controller, ascii carriage return <\r> ends it


#function which reads the current temperature of the controller
def temp_view():
        ser.close()
        ser.open()


        send_val = '*01000021\r'
        ser.write(send_val)

        read_val = ser.read(16)
        read_val = int(read_val[1:5], 16)
        read_val = str(read_val)

	    
        out_val = str(read_val[0:2]+'.'+read_val[2:4])

        return out_val

            

        ser.close()




#function which sends a temperature for the controller to set
# <01c> is command to initialize controller temp set 
def temp_set(val_in):
    
    val_in = val_in * 100
    send_val = str(0)
    checksum = 0

    if val_in < 0:
        compli = (2**16)-abs(val_in)
        hex_val = '1c%0*x' % (4,compli)

        
        for n in range(0, len(hex_val)):
            i = hex_val[n]
            i = ord(i)
            checksum += i
        checksum = str(hex(checksum))
        checksum = checksum[len(checksum)-2:len(checksum)]

        send_val = str('*'+hex_val+checksum+'\r')



    else:
        hex_val = '1c%0*x' % (4,val_in)


        for n in range(0, len(hex_val)):
            i = hex_val[n]
            i = ord(i)
            checksum += i
        checksum = str(hex(checksum))
        checksum = checksum[len(checksum)-2:len(checksum)]



        send_val = str('*'+hex_val+checksum+'\r')


    ser.close()
    ser.open()
    ser.write(send_val)
    #print ser.read(16)
    ser.close

