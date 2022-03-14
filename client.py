from pydoc import cli
import socket

host = '127.0.0.1'
port = 8090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(('127.0.0.1',5555))

client.connect((host,port))

while True:
	msg = input()
	client.send(msg.encode())
