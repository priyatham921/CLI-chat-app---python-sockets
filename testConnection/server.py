import socket
s = socket.socket()         
s.bind(('127.0.0.1', 8090))#192.168.0.166
s.listen(0)                 
 
while True:
 
    client, addr = s.accept()
 
    while True:
        content = client.recv(32)
 
        if len(content) ==0:
           break
 
        else:
            print(content)
 
    print("Closing connection")
    client.close()