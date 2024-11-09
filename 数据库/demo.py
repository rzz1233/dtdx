from pymysql import *
conn = connect(host="127.0.0.1",port=3306,user="root",password="221266",database="cart",charset="utf8")
cursor = conn.cursor()

cursor.execute("select shopping_name,shopping_price from shopping")
print(cursor.fetchall())
cursor.close()
conn.close()