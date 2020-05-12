import tkinter
root=tkinter.Tk()
root.title('图标')
tkinter.Label(root,text="lable").pack()
tkinter.Label(root,bitmap='error').pack()
root.mainloop()