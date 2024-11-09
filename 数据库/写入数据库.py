from pymysql import *
import openpyxl
conn = connect(host="127.0.0.1",port=3306,user="root",password="221266",database="student",charset="utf8")
cursor = conn.cursor()


wb = openpyxl.load_workbook("people.xlsx")
ws = wb["people"]

for row in ws.iter_rows(min_row=2,values_only=True):
    cursor.execute("INSERT INTO people VALUES (%s, %s, %s)", row)
    conn.commit()

cursor.close()
conn.close()