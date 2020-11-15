#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:02:12 2020

@author: trismonok
"""

import socket
import sys

# create a socket (coonnect two computer)
def create_socket():
    try:
        global host
        global port
        global s
        
        host = ""
        port = 9999
        s = socket.socket()
        
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        
        print("Binding the port " + str(port))
        
        s.bind((host,port))
        s.listen(5)
        
    except socket.error as msg:
        print("Socket binding error" + str(msg) + "\n" + "Retrying ...")
        
        # recursive function
        bind_socket()
        
# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! | IP " + address[0] + " | Port " + str(address[1]))
    send_command(conn)
    conn.close()


# Send commands to client
def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quit" or cmd=="exit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

# main finction
def main():
    create_socket()
    bind_socket()
    socket_accept()
    
# run main function:
main()

        
        