import urllib2
import json
url = 'https://raw.githubusercontent.com/chihsuan/facebook-checkin/gh-pages/data/fb_checkin.json?token=AEJJvZ6t08YEXOc2RZa56u7ku9SxWaaYks5Xv9vQwA%3D%3D'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()
r = json.loads(html)
for i in range(len(r)):
	print r[i]['id']+"\t"+r[i]['pageUrl']
