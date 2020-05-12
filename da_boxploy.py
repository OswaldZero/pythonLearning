import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt #导入图像库
value=[13, 15, 16,16,19 ,20 , 20, 21,22, 22, 25,25 ,25 ,25,30,
33, 33,35,35,35,35,36,40,45 ,46,52,70] 
data=DataFrame(value)
plt.figure() #建立图像
p=data.boxplot(return_type='dict') #画箱线图，直接使用DataFrame方法
x=p['fliers'][0].get_xdata() #'flies' 为异常值标签
y=p['fliers'][0].get_ydata()
y.sort() #从小到大排序，该方法直接改变原对象
#用annotate添加注释
for i in range (len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[1])) 
    else :
        plt.annotate(y[i],xy=(x[i],y[i]),xytext= (x[i]+0.08,y[i]))
plt.show()
