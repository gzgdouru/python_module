#coding:utf8
'''
9.返回指定索引的项
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
for i in range(10):
    lb.insert(END, str(i*100))
print lb.get(2, 7)
lb.pack()
root.mainloop()