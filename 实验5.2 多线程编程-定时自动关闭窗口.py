import time
import threading
import tkinter

#创建窗口，设置大小和标题
root=tkinter.Tk()
root.title('倒计时自动关闭窗口')
root.geometry('400x350')
root.resizable(False,False) #不允许改变窗口

#创建Text组件，放置文字
text=tkinter.Text(root,width=380)
text.place(x=10,y=10,width=380,height=230)
text.insert('0.0','假设阅读这些文字需要10秒钟时间')

#显示倒计时的Label
def autoClose1():
    time1=tkinter.Label(root, fg='red', anchor='w')
    time1.place(x=10,y=250,width=150)
    for i in range(10):
        time1['text']='距离窗口关闭还有{}秒'.format(10-i)
        time.sleep(1)
    root.destroy()

def autoClose2():
    time2=tkinter.Label(root, fg='green', anchor='w')
    time2.place(x=10,y=270,width=150)
    for i in range(20):
        time2['text']='距离窗口关闭还有{}秒'.format(20-i)
        time.sleep(1)
    root.destroy()
    
def autoClose3():
    time3=tkinter.Label(root, fg='blue', anchor='w')
    time3.place(x=10,y=290,width=150)
    for i in range(30):
        time3['text']='距离窗口关闭还有{}秒'.format(30-i)
        time.sleep(1)
    root.destroy()
#创建并启动线程
t=threading.Thread(target=autoClose1)
t.start()
t=threading.Thread(target=autoClose2)
t.start()
t=threading.Thread(target=autoClose3)
t.start()
root.mainloop()