import urllib2


req = urllib2.Request('http://www.google.co.uk')

try: urllib2.urlopen(req)

except urllib2.URLError as e:

	print e.reason

else:
	print 'site is up'