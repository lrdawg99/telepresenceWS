import socket
import thread
from collections import deque

#controller thread
def start_controller_client(q, b):
        #controller socket
        HOST = ''
        PORT = 51007
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))

        #Forever
        while True:
                s.listen(1)
                conn, addr = s.accept()
                print 'Controller connected by', addr
                while 1:
                        data = conn.recv(1024)
                        if not data: break
                        conn.send(data + " added to the task queue.")
                        q.append(data);
        conn.close()

#receiver thread
def start_receiver_client(q, b):
        #controller socket
        HOST = ''
        PORT = 51008
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        #Forever
        while True:
                s.listen(1)
                conn, addr = s.accept()
                print 'Receiver connected by', addr
                if len(q) <= 0:
                        conn.send('no_tasks');
                elif len(q) > 1:
                    #data = conn.recv(1024)
                    #if not data: break
                    response = '';
                    while len(q) > 0:
                        response += q.popleft()
                        if len(q) != 0:
                                response += ','
                    conn.send(response)
                else:
                    conn.send(q.popleft())
        conn.close()

