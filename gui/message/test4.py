#coding:utf8
'''
4.message绑定变量
'''
from Tkinter import *

root = Tk()
v = StringVar()
v.set(0.00)
for i in range(10):
    Message(root, text="A", textvariable=v).pack()
root.mainloop()