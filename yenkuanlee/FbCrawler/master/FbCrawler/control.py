import os
import time
while True:
	os.system("python InfluxPost/VoltToInflux.py")
	os.system("/home/voltdb/voltdb/bin/sqlcmd --query='delete from idlike;'")

	Slist = ["10","11","12","13","15","16"]
	for s in Slist:
		os.system("sshpass -p 'voltdb' ssh voltdb@10.0.10."+s+" 'python /home/voltdb/yenkuanlee/FbCrawler/vdb_get_data.py &> nouhpFB.txt &'")
	time.sleep(1800)
