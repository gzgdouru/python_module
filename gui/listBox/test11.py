#coding:utf8
'''
11.判断一个项是否被选中，使用索引
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END, str(i*100))
lb.select_set(3, 8)
print lb.select_includes(8)
print lb.select_includes(0)
lb.pack()
root.mainloop()