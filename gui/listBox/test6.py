#coding:utf8
'''
6.删除Listbox中的项，使用delete，这个函数也有两个参数，第一个为开始的索引值；第二个为结束的索引值，如果不指定则只删除第一个索引项
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END, i)
lb.delete(1, 3)
lb.pack()
root.mainloop()