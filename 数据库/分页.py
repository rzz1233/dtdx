from pymysql import *
conn = connect(host="127.0.0.1",port=3306,user="root",passwd="221266",db="student",charset="utf8")
cursor = conn.cursor()
n = 1
m = 3
# offset = (n-1)*m
cursor.execute("select * from people where score = 100 limit %s,%s",((n-1)*m,m))
res = cursor.fetchall()
for i in res:
    print(i)
cursor.close()
conn.close()