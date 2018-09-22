#coding:utf8
'''
3.设置spinbox的值,设置属性values,设置此值后,每次更新将使用values指定的值
'''
from Tkinter import *

root = Tk()
sb = Spinbox(root,
        values=(0, 2, 20, 40, -1),
        )
sb.pack()
print sb["values"]
root.mainloop()