#!/usr/bin/env python

# This code by paranoid.rat on Adafruit Forums, modified by pmft project

import sys
import subprocess
import serial
import argparse
import time

# path to the real avrdude
AVRDUDE_PATH = "\"C:\\Program Files (x86)\\pmft"

# real name of avrdude
AVRDUDE_NAME="avrdude-pmft\""

# prepare argument parser to understand -P PORT
parser = argparse.ArgumentParser()
parser.add_argument("-P", dest="port")
# parse only known parameters
args = parser.parse_known_args()

# if port argument is present perform soft reset
if args[0].port:
  try: # try to initiate serial port connection on PORT with 1200 baudrate
    ser = serial.Serial(
      port=args[0].port,
      baudrate=1200,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS
    )
  except serial.SerialException, e:
    print "pySerial error: " + str(e) + "\n"
    sys.exit(1)

  try: # try to open PORT
    ser.isOpen()
  except serial.SerialException:
    print "pySerial error: " + str(e) + "\n"
    sys.exit(1)

  # and close it immediately signaling to bootloader that flashing is imminent
  ser.close()

  # wait 2 second to ensure Arduino is ready
  time.sleep(2)

  # args is a tuple with parsed -P PORT and the rest of the arguments, so it needs to be join back
  avrdude_args=" ".join(str(x) for x in args[1]) + " -P" + args[0].port

else: # if no port argument is present
  # join all other arguments to be ready for avrdude invokation
  # avrdude_args=" ".join(str(x) for x in args[1])
  defaultport = "COM0"
  print("No port provided, using COM0...")
  try: # try to initiate serial port connection on PORT with 1200 baudrate
    ser = serial.Serial(
      port=defaultport,
      baudrate=1200,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS
    )
  except serial.SerialException, e:
    print "pySerial error: " + str(e) + "\n"
    sys.exit(1)

  try: # try to open PORT
    ser.isOpen()
  except serial.SerialException:
    print "pySerial error: " + str(e) + "\n"
    sys.exit(1)

  # and close it immediately signaling to bootloader that flashing is imminent
  ser.close()

  # wait 2 second to ensure Arduino is ready
  time.sleep(2)

  # args is a tuple with parsed -P PORT and the rest of the arguments, so it needs to be join back
  avrdude_args=" ".join(str(x) for x in args[1]) + " -P" + defaultport

try: # try to invoke avrdude passing all the options
  subprocess.check_call(AVRDUDE_PATH + "\\" + AVRDUDE_NAME + " " + avrdude_args, shell=True)
except subprocess.CalledProcessError, e: pass
#  print "avrdude error:\n", e.output
#  sys.exit(2)

sys.exit()
