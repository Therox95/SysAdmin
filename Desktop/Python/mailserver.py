from psutil import cpu_percent, net_io_counters
from time import sleep
import smtplib
import string
MAX_NET_USAGE = 400000
MAX_ATTACKS = 4
attack = 0
counter = 0
while attack <= MAX_ATTACKS:
	sleep(4)
	counter = counter + 1
	if cpu_percent(interval = 1) > 70:
		attack = attack + 1
	neti1 = net_io_counters()[1]
	neto1 = net_io_counters()[0]
	sleep(1)
	neti2 = net_io_counters()[1]
	neto2 = net_io_counters()[0]
	net = ((neti2+neto2) - (neti1+neto1))/2
	if net > MAX_NET_USAGE:
		attack = attack + 1
	if counter > 25:
		attack = 0
		counter = 0
TO = "you@your_email.com"
FROM = "webmaster@your_domain.com"
SUBJECT = "Your domain is out of system resources!"
text = "Go and fix your server!"
BODY = string.join(("From: %s" %FROM,"To: %s" %TO,"Subject: %s" %SUBJECT, "",text), "\r\n")
server = smtplib.SMTP('127.0.0.1', 1025)
server.sendmail(FROM, [TO], BODY)
server.quit