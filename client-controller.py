import socket
import sys
from configobj import ConfigObj

#Configuration
config = ConfigObj('system.conf')
HOST = config['HOST']
PORT = int(config['CONTROLLER_PORT'])

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	#Get the *second* command line argument. First is name of the script.
	a = sys.argv[1]
	s.send(a)
	
	#Listen for a response from the intermediary. (1024 byte max)
	data = s.recv(1024)
	s.close()
	print 'Received', repr(data)
except Exception, e:
	print 'Connection failed: ' + str(e)
	sys.exit()
