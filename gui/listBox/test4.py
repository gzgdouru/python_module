#coding:utf8
'''
4.使用selectmode = EXPANDED使用Listbox来支持Shift和Control
'''
from Tkinter import *

root = Tk()
lb = Listbox(root, selectmode=EXTENDED)
for item in ["python", "tkinter", "widget"]:
    lb.insert(END, item)
lb.pack()
root.mainloop()