#coding:utf8
'''
7.选中操作函数，使用函数实现。selection_set函数有两个参数第一个为开始的索引；第二个为结束的索引，如果不指定则只选中第一个参数指定的索引项
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END, i)
lb.select_set(0, 10)
lb.select_clear(3,5)
lb.pack()
root.mainloop()