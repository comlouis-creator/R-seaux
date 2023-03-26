#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 08:37:32 2021

@author: lmorlotpinta
"""

import socket
import datetime
#Time datetime

#def serveur():
TCP_IP = '127.0.0.1'
TCP_PORT = 5010
BUFFER_SIZE = 20

monsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
monsocket.bind((TCP_IP, TCP_PORT))
monsocket.listen(1) #on se place en écoute
    
    #conn, addr = monsocket.accept()
    #print('Connection address:')
    
while 1:
    conn, addr = monsocket.accept()
    print('Connection address:')
    data = conn.recv(BUFFER_SIZE)
    if not 'GET' in data: #on regarde si on ne trouve pas GET
        break
    File = data.split(', ')[2]
    path = ''
  #   try:
 #       with .path.(File): pass
  #   except:
  #       print()
        
    try:
        with open(File): pass
    except:
        print("Ca n'a pas fonctionnné !")
        
    print("received data:"), data
    now = datetime.now() #on capture l'heure à l'instant où cette ligne est executee
    #heure = "heure" + now strtime('%h%d%m') str(time.time())
    message = "HTTP/1.0 200 OK\r\nContent-Type:text/html\r\nContent-Length:37\r\n\r\n<HTML><BODY>Hello world</BODY></HTML>\r\n"#+heure+
    conn.send(message,data) # echo
    conn.send(message.encode())
    conn.close()
    
monsocket.close()
