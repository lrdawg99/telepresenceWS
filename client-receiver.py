import socket
import sys
import serial
import time

#Configuration
HOST = 'slopfest.net'    # The remote host
PORT = 51008              # The same port as used by the server
arduino = '/dev/tty.usbmodem612'
baud = 9600

#Connection to the intermediary server
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	data = s.recv(1024)
	s.close()
	print 'Received', repr(data)
except Exception, e:
	print 'Connection to intermediary server failed: ' + str(e)
	sys.exit()


else:
	#Analyze the output and fire the serial commmands to our connected device
	try:
		ser = serial.Serial(arduino, baud)	
	except Exception, e:
		print 'Connection to Arduino failed: ' + str(e)	
	else:
		print 'Connected to device! (on ' + arduino + ' with ' + baud ' baud rate)'
		#print ser
		time.sleep(0.1) #seconds
		print "Sending serial data to device."
		ser.write(data) #our received data
