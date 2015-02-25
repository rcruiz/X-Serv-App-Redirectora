#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Aplicacion redirectora
Rosa Cristina Ruiz Rivas
Alumna de SAT
"""

import socket
import random

# Crea un socket sobre TCP y se conecta a un determinado puerto
port = 1234
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', port))

# Podra escuchar hasta 5 conexiones TCP
mySocket.listen(5)

# Acepta las conexiones, lee datos entrantes y responde en una pagina HTML
try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        # Genera las URLs aleatorias
        randomURL = str(random.randint(0, 1000000000))
        newURL = "http://localhost:" + str(port) + "/" + randomURL
        head = "<html><head>"
        # Espera 7 segs antes de redirigir
        head += '<meta http-equiv="Refresh" content="7;url=' + newURL + '">'
        head += "</head>"
        recvSocket.send("HTTP/1.1 303 See Others\r\n\r\n" + head +
                        "<body><p>" + "Va a ser redirigido en 7 segundos a: " +
                        newURL + "</p></body></html>" + "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
        print "Closing binded socket"
        mySocket.close()
