#coding:utf8
'''
1.创建一个简单的Radiobutton
'''
from tkinter import *

root = Tk()

Radiobutton(root, text="python", value=0).pack()
Radiobutton(root, text="tkinter", value=1).pack()
Radiobutton(root, text="widget", value=2).pack()

root.mainloop()

#不指定绑定变量，每个Radiobutton自成一组
