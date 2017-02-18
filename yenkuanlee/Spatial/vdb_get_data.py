# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
from multiprocessing import Pool

def GetIdList():
	IdList = list()
	IdLink = dict()
	url = 'http://localhost:8080/api/1.0/'
	voltparams = json.dumps(["select * from spatial;"])
	httpparams = urllib.urlencode({
	    'Procedure': '@AdHoc',
	    'Parameters' : voltparams
	})
	data = urllib2.urlopen(url, httpparams).read()

	result = json.loads(data)
	for x in result['results'][0]['data']:
		IdList.append(x[0])
		IdLink[x[0]] = x[1]
	return IdList,IdLink
def InsertOneData(v1,v2):
        url = "http://10.0.10.21:8080/api/1.0/"
        voltparams = json.dumps([v1,v2])
        httpparams = urllib.urlencode({
            'Procedure': 'IdVisit.insert',
            'Parameters' : voltparams
        })
        data = urllib2.urlopen(url, httpparams).read()

IdList,IdLink = GetIdList()

def GetVisit(Uid):
	global IdLink
	url = IdLink[Uid]
	try:
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		html = response.read()
		SS = "</a></td></tr></tbody></table></div></div></div></div></div></div></div>"
		if SS in html:
			tmp = html.split(SS)[0].split("r=111\" rel=\"dialog\" role=\"button\">")
			people_count =  tmp[len(tmp)-1].split(" ")[0].replace(",","")
			#print str(Uid)+"\t"+str(people_count)
			InsertOneData(Uid,int(people_count))
	except:
		pass
p = Pool(20)
p.map(GetVisit,IdList)
#print IdList[0]
