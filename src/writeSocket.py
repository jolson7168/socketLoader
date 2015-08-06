#!/usr/bin/env python


import time
import datetime 
import random
import socket

 
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	t=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	sock.sendto(t+","+str(random.randint(1, 10))+","+str(random.randint(1, 10))+","+str(random.randint(1, 10))+","+str(random.randint(1, 10))+"\n", (UDP_IP, UDP_PORT))