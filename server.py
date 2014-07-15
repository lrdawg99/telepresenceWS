import socket
import thread

#start two threads: one socket for the controller client (50007), one socket for the robot client (50008)

#controller thread
def start_controller_client():
	#controller socket
	HOST = ''                 # Symbolic name meaning the local host
	PORT = 50007              # Arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	print 'Connected by', addr
	while 1:
	    data = conn.recv(1024)
	    if not data: break
	    conn.send(data)
	conn.close()

#reciever thread
def start_controller_client():
	#controller socket
	HOST = ''                 # Symbolic name meaning the local host
	PORT = 50008              # Arbitrary non-privileged port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	print 'Connected by', addr
	while 1:
	    data = conn.recv(1024)
	    if not data: break
	    conn.send(data)
	conn.close()