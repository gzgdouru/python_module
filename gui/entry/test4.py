#coding:utf8
'''
4.设置为密码输入框
'''
from Tkinter import *

root = Tk()

e = StringVar()
entry = Entry(root, textvariable=e)
e.set("input your text here")
entry.pack()

for mask in ["*", "#", "$"]:
    e = StringVar()
    entry = Entry(root, textvariable=e)
    e.set("passwd")
    entry.pack()
    entry.configure(show=mask)

root.mainloop()