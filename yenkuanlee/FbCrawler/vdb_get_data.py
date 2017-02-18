import urllib
import urllib2
import json
from multiprocessing import Pool

def GetIdList():
	IdList = list()
	IdLink = dict()
	url = 'http://localhost:8080/api/1.0/'
	voltparams = json.dumps(["select * from idlink;"])
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
def InsertOneData(v1,v2,v3):
        url = "http://10.0.10.10:8080/api/1.0/"
        voltparams = json.dumps([v1,v2,v3])
        httpparams = urllib.urlencode({
            'Procedure': 'IdLike.insert',
            'Parameters' : voltparams
        })
        data = urllib2.urlopen(url, httpparams).read()

IdList,IdLink = GetIdList()
def GetLike(Uid):
	global IdLink
	url = IdLink[Uid]
	try:
	        request = urllib2.Request(url)
        	response = urllib2.urlopen(request,timeout=1)
	        html = response.read()

        	tmp1 = html.split("renderLikesData")[1].split("]]")[0].split(",")
	        a =  tmp1[len(tmp1)-2].split("]")[0]
        	tmp2 = html.split("renderPTATData")[1].split("]]")[0].split(",")
	        b =  tmp2[len(tmp2)-2].split("]")[0]
		#print str(Uid)+"\t"+a+"\t"+b
		InsertOneData(Uid,int(a),int(b))
	except:
		#print Uid
		pass

#Tlist = list()
#for i in range(100):
#	Tlist.append(IdList[i])
p = Pool(8)
p.map(GetLike,IdList)
