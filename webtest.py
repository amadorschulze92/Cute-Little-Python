import socket
import sys
from urllib2 import urlopen, URLError, HTTPError

socket.setdefaulttimeout( 60 )  # timeout in seconds
loop = 0
count = 0
url = 'https://github.com/search?o=desc&q=repos%3A%3E%3D1&ref=searchresults&s=&type=Users&utf8=%E2%9C%93'

def test(url, count, loop):
	try :
		response = urlopen( url )
	except HTTPError, e:
		print 'Server couldn\'t fulfill request. Reason:', str(e.code)
		sys.exit()
	except URLError, e:
		print 'Failed to reach server. Reason:', str(e.reason)
		sys.exit()
	else :
		html = response.read()
		print 'HIT'
		print count
    
while loop == 0:
	count += 1
	test(url, count, loop)