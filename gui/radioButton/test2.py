#coding:utf8
'''
2.创建一个Radiobutton组，使用绑定变量来设置选中哦的按钮
'''
from Tkinter import *

root = Tk()

v = IntVar()
v.set(2)
for i in range(3):
    Radiobutton(root, variable=v, text="python", value=i).pack()

root.mainloop()