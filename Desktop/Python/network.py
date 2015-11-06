import datetime
import time
import socket
import os
import psutil

while True:

	print "starting"

	fh = open("mybytesrecieved.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(psutil.net_io_counters().bytes_recv) + "\n")
	fh.close()

	time.sleep(10)

	fh = open("mybytesrecieved.txt", "a")
	fh.write(str(datetime.datetime.now()) + "\n")
	fh.write(str(psutil.net_io_counters().bytes_recv) + "\n")
	fh.close()

	print "done"

