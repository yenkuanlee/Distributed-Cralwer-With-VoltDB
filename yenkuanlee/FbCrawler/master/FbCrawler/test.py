import urllib2
import socket
try:
    response = urllib2.urlopen('http://www.google.com', timeout=1)
except :
    print "Oops, timed out?"
