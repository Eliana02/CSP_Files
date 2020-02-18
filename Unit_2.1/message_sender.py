import socket

ip_address = '10.61.52.157'
port = 5000
buffer = 1024
message = 'Hello'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))
s.send(message.encode())

s.close()

