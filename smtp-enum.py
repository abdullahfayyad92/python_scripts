#!/usr/bin/python
import sys  
import socket 
if len(sys.argv) != 3:
        print (f"usage : {sys.argv[0]} <ip> <user> ")
ip = sys.argv[1]
users = open(sys.argv[2],'r')
users1 =[]
print ("step2")

for i in users.readlines():
        as_list=i.split(",")
        users1.append(as_list[0].replace("\n",""))

s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
connect = s.connect((ip,25))
banner = s.recv(1024)
	
print (banner)
for user in users1:
    #print (user)
    request = 'VRFY '+ user + '\r\n'
    s.send(request.encode())
    result = s.recv(1024)
    print ('\n')
    print (result)

s.close()
