#!/usr/bin/env python

import socket
import os


UDP_IP = '127.0.0.1'
UDP_PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
path = '/mnt/data'
while True:
    allFiles = os.listdir(path)
    for aFile in allFiles:
        if '.json' in aFile:
            f = open(path+'/'+aFile, 'r')
            for line in f:
                if len(line)>100:
                        sock.sendto(line, (UDP_IP, UDP_PORT))
            f.close()
