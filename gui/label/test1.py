#coding:utf8
#1.Label的第一个例子,text属性使用方法
from Tkinter import *

#初始化Tk
root = Tk()
label = Label(root, text="hello Tkinter")
label.pack()
root.mainloop()
