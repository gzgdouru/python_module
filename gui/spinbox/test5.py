#coding:utf8
'''
5.设置回调函数
'''
from Tkinter import *

def printSpinbox():
    print "spinbox"

root = Tk()
sb = Spinbox(root, from_=0, to=10, command=printSpinbox)
sb.pack()
root.mainloop()