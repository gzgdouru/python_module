#coding:utf8
'''
3.如果同一个组中的按钮使用相同的value，则这两个按钮的工作方式完全相同
'''
from Tkinter import *

root = Tk()

v = IntVar()
v.set(1)

for i in range(3):
    Radiobutton(root, variable=v, value=1, text="python" + str(i)).pack()

for i in range(3):
    Radiobutton(root, variable=v, value=i, text="python" + str(2 + i)).pack()

root.mainloop()