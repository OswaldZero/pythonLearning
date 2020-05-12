import matplotlib.pyplot as plt
import numpy as np
import xlrd
#sin(x)+1和cos(x**2)+1曲线画图
x=np.linspace(0,10,1000)
y1=np.sin(x)+1
y2=np.cos(x**2)+1
plt.figure(figsize=(8,4))
plt.plot(x,y1,label='sinx+1',color='red',linewidth=2)
plt.plot(x,y2,label='cosx^2+1')
plt.xlabel('Time(s)')
plt.ylabel('volt')
plt.title("example")
plt.ylim(0,2.2)
plt.legend()
plt.show()
#date.xlsx表格数据可视化
data=xlrd.open_workbook('data.xlsx')
sh=data.sheet_by_name('Sheet1')
x=sh.col_values(0)
y=sh.col_values(2)
plt.plot(x,y,'.')
plt.show()