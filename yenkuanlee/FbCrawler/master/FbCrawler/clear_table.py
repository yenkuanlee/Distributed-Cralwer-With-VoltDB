import os
from multiprocessing import Pool
IpList = ['10','11','12','13','15','16']
def clear_table(s):
	sql = "delete from idlink;"
	#sql = "create table idlink(id bigint, link varchar);"
	os.system("/home/voltdb/voltdb/bin/sqlcmd --query='"+sql+"' --servers=10.0.10."+s)
p = Pool(8)
p.map(clear_table,IpList)
