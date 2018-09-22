#coding:utf8
'''
10.设置Button状态
normal/active/disabled
'''
from Tkinter import *

def statePrint():
    print "state"

root = Tk()

for r in ["normal", "active", "disabled"]:
    Button(root, text=r, state=r, width=30, command=statePrint).pack()

root.mainloop()