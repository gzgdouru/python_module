#coding:utf8
'''
3.使用aspect属性指定宽高比例
'''
from Tkinter import *

root = Tk()
for i in range(10):
    Message(root, text="A"*i, aspect=400).pack()
root.mainloop()

#默认情况向wider/height =1.5，可以使用aspect属性，设置为4，即宽为高的4倍，可以显示10个'A'
