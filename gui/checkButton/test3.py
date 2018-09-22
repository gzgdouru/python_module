#coding:utf8
'''
3.通过回调函数改变checkButton的显示文本text的值
'''
from tkinter import *

def callCheckButton():
    v.set("check Tkinter")

root = Tk()
v = StringVar()
v.set("check python")
Checkbutton(root, text="check python", textvariable=v, command=callCheckButton).pack()
root.mainloop()