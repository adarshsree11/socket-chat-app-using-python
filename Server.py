from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 12000))
server.listen()
print('server is listening at 12000')

connection, address =  server.accept()
print('server accepted request!')
