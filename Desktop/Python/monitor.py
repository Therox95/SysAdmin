import datetime
import time
import socket
import os

while True:

	print "starting"

	fh = open("myserverload.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(os.getloadavg()) + "\n")
	fh.close()

	time.sleep(30)

	fh = open("myserverload.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(os.getloadavg()) + "\n")
	fh.close()

	print "done"