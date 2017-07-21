#import time
import socket
import time
import sys
from urllib2 import urlopen, URLError, HTTPError

#start_time = time.time()
socket.setdefaulttimeout( 60 )  # timeout in seconds
loop = 0
count = 0
url = 'http://www.tripadvisor.com/Hotels-g28926-California-Hotels.html'

def test(url, count, loop):
	try :
		response = urlopen( url )
	except HTTPError, e:
		main ()
		#print("--- %s seconds ---" % (time.time() - start_time))
		print 'Server couldn\'t fulfill request. Reason:', str(e.code)
		sys.exit()
	except URLError, e:
		main ()
		#print("--- %s seconds ---" % (time.time() - start_time))
		print 'Failed to reach server. Reason:', str(e.reason)
		sys.exit()
	else :
		html = response.read()
		print 'HIT'
		print count
    
while loop == 0:
	time.sleep(0) # sleep for x seconds
	count += 1
	test(url, count, loop)