#3.8.2版本字符串的所有方法,还包括老师课件上的max(),min(),python基本函数
s="wyh"
#1 capitalize()字符串第一个字符转为大写
print(s.capitalize())
#2* casefold()所有变小写
print(s.casefold())
#3 返回填充后的字符串
print(s.center(5,"-"))
#4 count(substring,start,end),返回子字符串出现的个数
print(s.count("w",0,len(s)))
#5 指定编码方式
b=s.encode("utf-8","ignore")
print(b)
#6 解码
print(b.decode("utf-8","ignore"))
#7 看字符串是不是以这个结束
print(s.endswith("h",0,len(s)))
#8 把字符串里面的table转化为8个空格
print(s.expandtabs(8))
#9 寻找子字符串
print(s.find("y",0,len(s)))
#10 format()字符串自带的格式化函数
print("wyh {0} a student".format("is"))
#11 以字典等其他映射的方式格式化
student={"name":"wyh","age":"19"}
print("{name} is {age} years old".format_map(student))
#12 和find类似,如果不在报异常,find是返回-1
print(s.index("w"))
#接下来的方法和C++语言的<ctype>相同
#13 Return True if the string is an alpha-numeric string, False otherwise.
print(s.isalnum())
#14 Return True if the string is an alphabetic string, False otherwise.
print(s.isalpha())
#15 Return True if all characters in the string are ASCII, False otherwise.
print(s.isascii())
#16 Return True if the string is a decimal string, False otherwise.
print(s.isdecimal())
#17 Return True if the string is a digit string, False otherwise.
print(s.isdigit())
#18 Return True if the string is a valid Python identifier, False otherwise.
print(s.isidentifier())
#19 Return True if the string is a lowercase string, False otherwise.
print(s.islower())
#20 Return True if the string is a numeric string, False otherwise.
print(s.isnumeric())
#21 Return True if the string is printable, False otherwise.
print(s.isprintable())
#22 Return True if the string is a whitespace string, False otherwise.
print(s.isspace())
#23 判断是否为标题,标题就是首字母大写,其他为小写
print(s.istitle())
#24 Return True if the string is an uppercase string, False otherwise.
print(s.isupper())
#25 把s作为插入符,合成字符串
print(s.join(["sd","dfs","fsad"]))
#26 和center差不多,只不过是左对齐,右填充
print(s.ljust(5,"-"))
#27 Return a copy of the string converted to lowercase.
print(s.lower())
#28 返回删除前导空格的字符串副本。如果给定了chars而不是None，则改为删除chars中的字符。
print(s.lstrip())
#29 返回按照映射后的字符
table=s.maketrans("w","l")
print(s.translate(table))
#30 返回字符串中最大的字符,max()是python的函数,并不属于字符串的方法
print(max(s))
#31 min()同上
print(min(s))
#32 跟split有点像,但是不一样,无论如何返回三个元素的元组,s中找不到分隔符就元组的后两个元素为空
print(s.partition("z"))
#33 替换函数,可指定替换次数,默认为-1
print(s.replace("w","q"))
#34 从右边开始,和find方向相反,find是left,rfind是right
print(s.rfind("y"))
#35 同上解释类似
print(s.rindex("w"))
#36 与ljust方向相反
print(s.rjust(9,"x"))
#37 与partition方向搜索相反
print(s.rpartition("z"))
#38 与split方向相反
print(s.rsplit())
#38 与lstrip删除空格方向相反
print(s.rstrip())
#39 分割字符串,可指定分隔符和次数
print(s.split())
#40 以line boundaries(回车换行)为分割,可指定是否包括他们
print(s.splitlines())
#41 判断以什么开头
print(s.startswith("w"))
#42 及包含rstrip和lstrip
print(s.strip())
#43 swap case,大小化相反
print(s.swapcase())
#44 把一个字符串标题化
print(s.title())
#44 参考29条
#45 字符串全大写
print(s.upper())
#46 以零填充在左边,和rjust()中以0填充,指定宽度差不多
print(s.zfill(9))