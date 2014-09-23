'''webcamToFlickr project
Epic Jefferson 

based on the python flickr api tutorial
https://github.com/alexis-mignon/python-flickr-api/wiki/Tutorial
and adafruit's motion sensing lesson
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement
(we'll be adding the sensing part pretty soon)
'''

#!/usr/bin/env python
import sys
import os
import flickr_api
import time
import RPi.GPIO as io
from flickr_keys import *		#import your keys, this is in th flickr_api tutorial
io.setmode(io.BCM)

pir_pin = 18					#connect the PIR sensor to pin 18 on the Pi's GPIO
io.setup(pir_pin, io.IN)         # activate input

#get api key and api secret key
flickr_api.set_keys(api_key = FLICKR_API_KEY, api_secret = FLICKR_API_SECRET)

#get oauth_verifier
#a = flickr_api.auth.AuthHandler.load("verifier.txt")
flickr_api.set_auth_handler("verifier.txt")

while True:
    print(io.input(pir_pin))
    if io.input(pir_pin):
	os.system('sudo fswebcam -r 640x480 -S 20 webcam.jpg')
	flickr_api.upload(photo_file = "webcam.jpg", title = "Done IT!")
	time.sleep(5)
    time.sleep(0.25)
