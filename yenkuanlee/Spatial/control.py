import os
Slist = ["10","11","12","13","15","16","21"]
for s in Slist:
	os.system("sshpass -p 'voltdb' ssh voltdb@10.0.10."+s+" 'python /home/voltdb/yenkuanlee/Spatial/vdb_get_data.py &> nouhp.txt &'")
