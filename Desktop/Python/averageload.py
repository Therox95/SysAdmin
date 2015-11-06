import datetime
import time
import socket
import os
import psutil

while True:

	print "starting"

	fh = open("mycpuload.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(psutil.virtual_memory().percent) + "\n")
	fh.write(str(psutil.cpu_percent()) + "\n")
	fh.close()

	time.sleep(10)

	fh = open("mycpuload.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(psutil.virtual_memory().percent) + "\n")
	fh.write(str(psutil.cpu_percent()) + "\n")
	fh.close()

	print "done"