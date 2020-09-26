# Joshua Farren

# Web Server Socket

# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)


# Prepare a server socket
serverPort = 6250
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is prepared:', serverPort)

while True:
    # Establish the connection
    print('Ready to serve...')

     # Fill in start #Fill in end
    connectionSocket, addr = serverSocket.accept()

    try:
        print(addr)
        message = connectionSocket.recv(1024) # Fill in start #Fill in end
        # message.decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        messageOK = '\nHTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(messageOK.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        messageError = '\nHTTP/1.1 404 Not Found\n\n'
        connectionSocket.send(messageError.encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data