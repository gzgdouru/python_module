#coding:utf8
'''
4.spinbox绑定变量
'''
from Tkinter import *

root = Tk()
v = StringVar()
sb = Spinbox(root,
        values=(0, 2, 20, 40, -1),
        increment=2,
        textvariable=v
        )
v.set(200)
sb.pack()
print sb["values"]
root.mainloop()