import RPi.GPIO as GPIO
import time
import socket

# addressing information of target
IPADDR = '192.168.0.115'
PORTNUM = 2390

# initialize a socket
# SOCK_DGRAM specifies that this is UDP
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# enter the data content of the UDP packet as hex
RED 		= str(1023)+':'+str(0)+':'+str(0)
OFF 		= str(0)+':'+str(0)+':'+str(0)

GPIO.setmode(GPIO.BCM)

#set the GPIO input pins for touch sensor
pad0 = 22
pad1 = 10
pad2 = 9
pad3 = 24
pad4 = 23

GPIO.setup(pad0, GPIO.IN)
GPIO.setup(pad1, GPIO.IN)
GPIO.setup(pad2, GPIO.IN)
GPIO.setup(pad3, GPIO.IN)
GPIO.setup(pad4, GPIO.IN)

#light switches
light0 = False
light1 = False
light2 = False
light3 = False
light4 = False

pad0alreadyPressed = False
pad1alreadyPressed = False
pad2alreadyPressed = False
pad3alreadyPressed = False
pad4alreadyPressed = False

while True:
    pad0pressed = not GPIO.input(pad0)
    pad1pressed = not GPIO.input(pad1)
    pad2pressed = not GPIO.input(pad2)
    pad3pressed = not GPIO.input(pad3)
    pad4pressed = not GPIO.input(pad4)
    
    if pad0pressed and not pad0alreadyPressed:
		if light0:
			print "Pad 0 pressed. Turning Light on."
			# connect the socket
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
			s.connect((IPADDR, PORTNUM))
			# send the command
			s.send(RED)
			# close the socket
			s.close()
			light0 = False
		else:
			print "Pad 0 pressed. Turning Light off."
			# connect the socket
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
			s.connect((IPADDR, PORTNUM))
			# send the command
			s.send(OFF)
			# close the socket
			s.close()
			light0 = True
    pad0alreadyPressed = pad0pressed

    if pad1pressed and not pad1alreadyPressed:
        print "Pad 1 pressed"
    pad1alreadyPressed = pad1pressed

    if pad2pressed and not pad2alreadyPressed:
        print "Pad 2 pressed"
    pad2alreadyPressed = pad2pressed

    if pad3pressed and not pad3alreadyPressed:
        print "Pad 3 pressed"
    pad3alreadyPressed = pad3pressed

    if pad4pressed and not pad4alreadyPressed:
        print "Pad 4 pressed"
    pad4alreadyPressed = pad4pressed

    time.sleep(0.1)
