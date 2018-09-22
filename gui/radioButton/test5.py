#coding:utf8
'''
5.与Checkbutton类似，每个Radiobutton可以有自己的处理函数，每当点击按钮时，系统会调用相应的处理函数
'''
from Tkinter import *

root = Tk()

v = IntVar()
v.set(0)

def r1():
    print "call r1"

def r2():
    print "call r2"

def r3():
    print "call r3"

def r4():
    print "call r4"

for i, r in enumerate([r1, r2, r3, r4]):
    Radiobutton(root, variable=v, text="radio button", value=i, command=r).pack()
    Radiobutton(root, variable=v, text="radio button", value=i, command=r).pack()

root.mainloop()