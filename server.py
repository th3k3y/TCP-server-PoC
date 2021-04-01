#Importing required modules.

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Defining the main server socket object.

host = socket.gesthostbyname() #Getting the hostname.
port = 4444 #Or whatever port you want.

serversocket.bind((host, port)) #Binding the host and the port.
serversocket.listen(1) #Set this at how much connections you want. & Defining the listener.

while True:
	clientsocket, adress = serversocket.accept() #Accepting connections from the client.
	print("Successfully connected to " + str(adress)) #Saying that the connection has been successfully received.
	clientsocket.close() #Closing the socket.