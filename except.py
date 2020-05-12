#异常语法
try:
    print(8/0)
except  ZeroDivisionError as ze:
    print("除数不能为0")

try:
    print(8/5)
except ZeroDivisionError as zde:
    print("除数不能为0")
else:
    print("正常运行")
finally:
    print("异常示例")

#触发异常与自定义异常
def raiseEx():
    raise Exception("抛出异常")
raiseEx()

class selfException(Exception):
    pass

#返回异常
try:
    8/0
except:
    import sys
    t=sys.exc_info()
    for i in t:
        print(i)

