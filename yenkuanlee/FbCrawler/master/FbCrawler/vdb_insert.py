import urllib
import urllib2
import json
import sys
def InsertOneData(s,v1,v2):
	url = "http://10.0.10."+s+":8080/api/1.0/"
	voltparams = json.dumps([v1,v2])
	httpparams = urllib.urlencode({
	    'Procedure': 'IDLINK.insert',
	    'Parameters' : voltparams
	})
	data = urllib2.urlopen(url, httpparams).read()

Slist = ["10","10","11","13","15","15","16","16","16","16"]
IDlist = list()
f = open(sys.argv[1],'r')
while True:
	line = f.readline()
	if not line:break
	line = line.replace("\n","")
	IDlist.append(line)
cnt = 0
for i in range(len(IDlist)):
	InsertOneData(Slist[cnt%len(Slist)],int(IDlist[i].split("\t")[0]),IDlist[i].split("\t")[1])
	cnt += 1
