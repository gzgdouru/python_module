#coding:utf8
'''
5.向Listbox中添加一个item
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
for item in ["python", "tkinter", "widget"]:
    lb.insert(END, item)
lb.insert(0, ["windows", "linux", "unix"])
lb.insert(0, "windows", "linux", "unix")
lb.pack()
root.mainloop()
