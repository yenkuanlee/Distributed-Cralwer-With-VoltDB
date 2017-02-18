import urllib
import urllib2
import json
from multiprocessing import Pool
from influxdb import InfluxDBClient
import time
def GetIdLike():
	Jlist = list()
        IdList = list()
        IdLink = dict()
        url = 'http://localhost:8080/api/1.0/'
        voltparams = json.dumps(["select * from idlike;"])
        httpparams = urllib.urlencode({ 
            'Procedure': '@AdHoc',
            'Parameters' : voltparams
        })   
        data = urllib2.urlopen(url, httpparams).read()

        result = json.loads(data)
        for x in result['results'][0]['data']:
		Jtmp = {"measurement":"IdLike","tags":{"uid":x[0]},"fields":{"ulike":x[1], "utalk":x[2]}}
		Jlist.append(Jtmp)
        return Jlist

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'FB_CRAWLER')
try:
        client.create_database('FB_CRAWLER')
except:
        pass

Jtmp = GetIdLike()
print len(Jtmp)
client.write_points(Jtmp)
