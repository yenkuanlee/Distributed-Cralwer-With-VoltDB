# -*- coding: utf-8 -*-
import urllib2
import sys
def GetVisit(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	html = response.read()
	if " 人次造訪</a></td></tr></tbody></table></div></div></div></div></div></div></div> --></code></div>" in html:
		tmp = html.split(" 人次造訪</a></td></tr></tbody></table></div></div></div></div></div></div></div> --></code></div>")[0].split("r=111\" rel=\"dialog\" role=\"button\">")
		print tmp[len(tmp)-1]
	else:
		pass
		'''
		url = html.split("<input type=\"hidden\" autocomplete=\"off\" name=\"next\" value=\"")[1].split("\"")[0]
		if url[len(url)-1]=="/":
			url += "likes"
		else:
			url += "/likes"
		try:
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			html = response.read()
			tmp = html.split("renderTotalVisitsData")[1].split("]]")[0].split(",")
			print tmp[len(tmp)-2]
		except:
			print url
		'''
GetVisit(sys.argv[1])
