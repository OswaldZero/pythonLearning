import pymysql
co=pymysql.connect("localhost","root","1234","test2",charset="utf-8")
cx=co.cursor()
cx.execute("SELECT * FROM Teacher")
a=cx.fetchall()
print(a)
cx.close()
co.close()