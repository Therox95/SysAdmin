import datetime
import time
import socket
import os
import psutil

while True:

	print "starting"

	
	print (str(datetime.datetime.now()) + "\n")
	print (str(psutil.net_io_counters().bytes_recv) + "\n")
	
	firstbytes = psutil.net_io_counters().bytes_recv

	time.sleep(10)

	print (str(datetime.datetime.now()) + "\n")
	print (str(psutil.net_io_counters().bytes_recv) + "\n")

	secondbytes = psutil.net_io_counters().bytes_recv

	bytesper10second = secondbytes - firstbytes

	print bytesper10second

	print "done"

