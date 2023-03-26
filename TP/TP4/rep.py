#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 08:52:06 2021

@author: lmorlotpinta
"""

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = 'Hello'

Monsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Monsocket.connect((TCP_IP,5005))
Monsocket.send(bytes(MESSAGE,'utf-8'))
data = Monscoket.rcv(BUFFER_SIZE)

Monsocket.close()

print( data)