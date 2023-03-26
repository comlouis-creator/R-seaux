#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 08:07:35 2021

@author: lmorlotpinta
"""

import socket
url_site='www.univ-rennes1.fr'
BUFFER_SIZE = 1024
monsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
monsocket.connect((url_site,80))
monsocket.sendall(b"GET /index.html HTTP/1.0\r\n\r\n")
donnees = monsocket.recv(BUFFER_SIZE)
print(donnees)
monsocket.close()

