import urllib2
import urllib
import json
def GetIdList():
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
                print (x[0])
GetIdList()
