import pymysql

mysql = {}

mysql['host'] = "172.20.10.6"
mysql['port'] = 3306
mysql['user'] = "appuser"
mysql['passwd'] = "@Chenliujin8"
mysql['db'] = "stock"

conn = pymysql.connect(
  host=mysql['host'], 
  port=mysql['port'], 
  user=mysql['user'], 
  passwd=mysql['passwd'], 
  db=mysql['db'], 
  charset="utf8",
  autocommit = True
)

cursor = conn.cursor()


