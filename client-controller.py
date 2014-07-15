import socket
import sys

HOST = 'slopfest.net'    # The remote host
PORT = 51007              # The same port as used by the server

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.send('turnleft')
	data = s.recv(1024)
	s.close()
	print 'Received', repr(data)
except Exception, e:
	print 'Connection failed: ' + str(e)
	sys.exit()
