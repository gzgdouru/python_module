#coding:utf8
'''
4.上述的textvariable使用方法与Button的用法完全相同，使用此例是为了区别Checkbutton的另外的一个属性variable,
此属性与textvariable不同，它是与这个控件本身绑定，Checkbutton自己有值：On和Off值，缺省状态O为1，Off为0
'''

from tkinter import *

def callCheckButton():
    print(v.get())

root = Tk()
v = IntVar()
Checkbutton(root, text="checkbutton value", variable=v, command=callCheckButton).pack()
root.mainloop()
