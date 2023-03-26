#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:30:12 2021

@author: lmorlotpinta
"""

import socket

TCP_IP="148.60.3.86"
TCP_PORT=2004
BUFFER_SIZE=1024

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((TCP_IP,TCP_PORT))
sock.listen(1)
reponse="GET /test.html HTTP/1.1"
conn, addr = sock.accept()
print('Connection adress:', addr)
while 1:
    data=conn.recv(BUFFER_SIZE)
    if not data : break
    print("received data:", data)
    try:
        open("test.html")
    except:
        print("404 Not found")
    try:
    #    File f = open("test.html","r")
        texte = f.read("test.html","r")
    except:
        print("403 Forbidden")
    conn.send(bytes(reponse,'utf-8'))
conn.close()