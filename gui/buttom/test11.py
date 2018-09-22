#coding:utf8
'''
11.绑定Button与变量
设置Button在textvariable属性
'''
from Tkinter import *

root = Tk()

def changeText():
    if b["text"] == "text":
        v.set("change")
        print "change"
    else:
        v.set("text")
        print "text"

v = StringVar()
b = Button(root, textvariable=v, command=changeText)
v.set("text")
b.pack()

root.mainloop()