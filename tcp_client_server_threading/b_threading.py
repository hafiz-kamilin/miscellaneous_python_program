#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# setting up modules used in the program
from socket import socket
from socket import *
import threading
import socket
import time

server_status = True
client_status = True

# create a server class
class Server(threading.Thread):

    # initialize server socket
    def __init__(self, host1, port1):

        self.server_socket = socket.socket()
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host1, port1))
        self.server_socket.listen(0)
        self.connection, self.client_address = self.server_socket.accept()
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)
        self.receiving()

    # get input from client socket
    def receiving(self):

        try:

            while True:

                if (server_status != True):

                    break 

                user_input = int(self.connection.recv(1024).decode())
                print("a_threading: %d" % user_input)

        except:

            print ("\nConnection to b_threading client is closed.")

        finally:

            self.connection.close()
            self.server_socket.close()

# create a client class
class Client(threading.Thread):

    # initialize client socket
    def __init__(self, host2, port2):

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False 

        while not self.connected:

            try:

                self.client_socket.connect((host2, port2))
                self.connected = True

            except Exception as e:

                pass
                
        self.sending()

    # send input to server socket
    def sending(self):

        try:
                    
            while True:

                if (client_status != True):

                    break

                self.client_socket.send('1'.encode())
                time.sleep(1)
                self.client_socket.send('2'.encode())
                time.sleep(1)
                self.client_socket.send('3'.encode())
                time.sleep(1)
                self.client_socket.send('4'.encode())
                time.sleep(1)

        except:

            print ("Connection to b_threading server is closed.")

        else:
            
            self.client_socket.close()

# create threading class
class Threading(object):

    server_thread = threading.Thread(target = Server, args = ("127.0.0.1", 6006))
    client_thread = threading.Thread(target = Client, args = ("127.0.0.1", 5005))
    server_thread.daemon = True
    client_thread.daemon = True
    server_thread.start()
    client_thread.start()

    try:

        while True:

            if (server_thread.is_alive() != True or client_thread.is_alive() != True):

                break

    except KeyboardInterrupt:

        print ("Key interrupt detected.")

    finally:

        global server_status
        global client_status
        server_status = False
        client_status = False

if __name__ == '__main__':

    Threading()