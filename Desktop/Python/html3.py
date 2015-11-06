import urllib2


req = urllib2.Request('http://www.rgu.ac.uk/test.html')

try: urllib2.urlopen(req)

except urllib2.HTTPError as e:

	code = e.code
	if code == 200:
		print "AYE SOUND"
	elif code == 404:
		print "AWW NAWWW"
	else:
		print "FIX YOUR STUFF PAL"

except urllib2.URLError as e:

	print e.reason

else:
	print 'site is up'
	
	code = urllib2.urlopen(req).getcode()

	print code

