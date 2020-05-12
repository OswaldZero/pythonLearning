#count、mean、std、min、25%、50%、75%、max指标
import pandas as pd
while True:
    path=input("请输入路径:")
    try:
        data=pd.read_excel(path,index_col="姓名")
        print(data.describe())
        break
    except :
        print("重新输入路径")