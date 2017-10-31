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
colorList = []
colorList.append(str(0)+':'+str(0)+':'+str(0))
colorList.append(str(1023)+':'+str(0)+':'+str(0))
colorList.append(str(0)+':'+str(0)+':'+str(1023))
colorList.append(str(0)+':'+str(1023)+':'+str(0))
colorList.append(str(1023)+':'+str(1023)+':'+str(1023))

# color index
i = 0

# Timing delay to check for double tap
delay = 0.3

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

def changeColor( color ):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	s.connect((IPADDR, PORTNUM))
	s.send(colorList[color])
	s.close()
	i = color

while True:
    pad0pressed = not GPIO.input(pad0)
    pad1pressed = not GPIO.input(pad1)
    pad2pressed = not GPIO.input(pad2)
    pad3pressed = not GPIO.input(pad3)
    pad4pressed = not GPIO.input(pad4)
    
    if pad0pressed and not pad0alreadyPressed:
		while True:
			time.sleep(delay)
			pad0pressedAgain = not GPIO.input(pad0)
			if pad0pressedAgain:
				print "Pad 0 double tapped. Turning Light blue."
				changeColor(2)
				light0 = True
			break
		if not light0:
			print "Pad 0 pressed. Turning Light red."
			changeColor(1)
			light0 = True
		elif light0 and not pad0pressedAgain:
			print "Pad 0 pressed. Turning Light off."
			changeColor(0)
			light0 = False
    pad0alreadyPressed = pad0pressed
    pad0pressedAgain = pad0pressed

    if pad1pressed and not pad1alreadyPressed:
		print "Pad 1 pressed changing color"
		print 'i:'+str(i)
		i = (i+1) % len(colorList)
		print 'i:'+str(i)
		print str(len(colorList))
		print 'i:'+str(i)
		if i == 0:
			i+=1
		print 'i:'+str(i)
		changeColor(i)
		light0 = True
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
