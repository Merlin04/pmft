#!/usr/bin/python2
import os
import sys
pwd = os.getcwd()
print("pmft v0.1")
if (sys.argv[1] == "help"):
    print("Usage: pmft.py [hex file path] [port]")
    sys.exit()
filepath = sys.argv[1]
if (sys.argv[2]):
    port = sys.argv[2]
    os.system("python \"C:\\Program Files (x86)\\pmft\\pmft-flasher.py\" -p atmega32u4 -c avr109 -C \"C:\\Program Files (x86)\\pmft\\avrdude-pmft\\avrdude-pmft.conf\" -P " + port + " -U flash:w:" + pwd + "/" + filepath + ":i")
else:
    os.system("python \"C:\\Program Files (x86)\\pmft\\pmft-flasher.py\" -p atmega32u4 -c avr109 -C \"C:\\Program Files (x86)\\pmft\\avrdude-pmft\\avrdude-pmft.conf\" -U flash:w:" + pwd + "/" + filepath + ":i")
