#coding:utf8
'''
10.返回当前返回的项的索引，不是item的值
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END, str(i*100))
lb.select_set(3, 8)
print lb.curselection()
lb.pack()
root.mainloop()