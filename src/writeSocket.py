#!/usr/bin/env python

import socket
import os
from ConfigParser import RawConfigParser



def getCmdLineParser():
    import argparse
    desc = 'Set up a streaming data source'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-c', '--config_file', default='../config/writeSocket.cfg',
                        help='configuration file name (*.ini format)')

    return parser



if __name__ == '__main__':

    p = getCmdLineParser()
    args = p.parse_args()
    cfg = RawConfigParser()
    cfg.read(args.config_file)
    UDP_IP = cfg.get('newtwork','hostname')
    UDP_PORT = int(cfg.get('newtwork','port'))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.listen(5)
    path = cfg.get('data','datapath')
    minLength = int(cfg.get('data','minlength'))
    extension = cfg.get('data','extension')
    while True:
        (clientsocket, address) = sock.accept()
        allFiles = os.listdir(path)
        for aFile in allFiles:
            if extension in aFile:
                f = open(path+'/'+aFile, 'r')
                for line in f:
                   if len(line) > minLength:
                       clientsocket.sendto(line, (UDP_IP, UDP_PORT))
                f.close()
