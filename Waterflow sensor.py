import RPi.GPIO as GPIO
import time, sys


FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

global count
count = 0

def countPulse(channel):
   global count
   count = count+1
   print count

GPIO.add_event_detect(FLOW_SENSOR, GPIO.BOTH, callback=countPulse)


while True:
    try:
        print(GPIO.input(23))
	print (count)
        time.sleep(1)
	
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!'
        GPIO.cleanup()
        sys.exit()
#flow = count / (60 * 7.5)
