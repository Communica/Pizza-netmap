#!/usr/bin/python
import serial
import sys
import ping
import time
import random


ser = serial.Serial('/dev/tty.usbmodem641', 9600)

watch = {
	"10.13.37.6": '7', 
	"10.13.37.1": '5',  
	"10.13.37.2": '6', 
	"10.13.37.3": '2', 
	"10.13.37.4": '3',
	"10.13.37.5": '4'
	}

lost = {}

count = 8

################################
#	MONITORING
################################


def clean_the_mess_up_after_you():
	ser.close()


def tellThePizza(switch):
	"""	Flipping the switch-status. """
	if not switch in lost:
		print "Switch %s is down :(" % switch
		lost[switch] = watch[switch]
		n = watch[switch]
		ser.write( n )

def weGotMorePizzaAgain(switch):
	"""	A switch has come back up to life """
	if switch in lost:
			del lost[switch]
			ser.write(watch[switch])


try:
	while 1:
		for switch in watch:

			we_have_attempts_left = count
			we_belive_its_down = True

			#if  ping.do_one(switch, 0.5) == None: print "POWER DOWN!!!", switch  
			while we_belive_its_down and we_have_attempts_left:
				
				we_have_attempts_left -= 1


				try:
					if not ping.do_one(switch, 0.5) == None:
		
						we_belive_its_down = False	#got reply from switch :). Phew!
						weGotMorePizzaAgain(switch)

				except Exception as e:
					print "No Internetz", e

			
			if we_belive_its_down:
				# If we arrive here, the switch is down!
				tellThePizza(switch)
		

		#	And now we wait some.	
		time.sleep(random.randrange(30))
except KeyboardInterrupt:
	clean_the_mess_up_after_you()
except Exception as e:
	print e
	clean_the_mess_up_after_you()
finally:
	pass





