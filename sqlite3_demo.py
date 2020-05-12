import sqlite3
connect=sqlite3.connect("F:/wyh/test.db")
cursor=connect.cursor()
cursor.execute("CREATE Table Course(CNo char(4) PRIMARY KEY,CName varchar(50) not null,CCredits decimal(4,1) default(4),CTime decimal(3,0),CTerm char(11))")
cursor.execute("INSERT INTO Course(CNo,CName,CTime,CTerm) VALUES ('0003','数据结构',54,'2')" )
cursor.execute("INSERT INTO Course VALUES(?,?,?,?,?)",('0001','英语',2,36,'2'))
a=[('0002','高等数学',3,36,'2'),('0004','C语言',3,54,'2')]
cursor.executemany("INSERT INTO Course VALUES (?,?,?,?,?)",a)
connect.commit()


connect=sqlite3.connect("F:/wyh/test.db")
cursor=connect.cursor()
cursor.execute("SELECT * FROM Course ORDER BY CNo")
print(cursor.fetchone())
print(cursor.fetchall())