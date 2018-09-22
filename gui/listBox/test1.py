#coding:utf8
'''
1.创建一个Listbox，向其中添加三个item
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
for item in ["python", "tkinter", "widget"]:
    lb.insert(END, item)
lb.pack()
root.mainloop()
