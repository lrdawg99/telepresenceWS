import socket
import sys
import serial
import time
from configobj import ConfigObj

#Configuration
config = ConfigObj('system.conf')
HOST = config['HOST']
PORT = int(config['RECEIVER_PORT'])
arduino = config['ARDUINO'] 
baud = int(config['BAUD'])

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
	if (data == "no_tasks"):
		#No reason to connect to device!
		print('Bye bye!')
		sys.exit()
	try:
		ser = serial.Serial(arduino, baud)	
	except Exception, e:
		print 'Connection to Arduino failed: ' + str(e)	
	else:
		print 'Connected to device! (on ' + arduino + ' with ' + str(baud)  + ' baud rate)'
		#print ser
		time.sleep(0.1) #seconds
		print "Sending serial data to device."
		ser.write(data) #our received data
		print 'All done.'
		print 'Bye bye!'
