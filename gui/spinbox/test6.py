#coding:utf8
'''
6.打印spinbox的当前内容
'''
from Tkinter import *

def printSpinbox():
    print sb.get()

root = Tk()
sb = Spinbox(root, from_=0, to=10, command=printSpinbox)
sb.pack()
root.mainloop()