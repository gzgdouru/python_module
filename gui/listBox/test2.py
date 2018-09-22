#coding:utf8
'''
2.创建一个可以多选的Listbox,使用属性selectmode
'''
from Tkinter import *

root = Tk()
lb = Listbox(root, selectmode=MULTIPLE)
for item in ["python", "tkinter", "widget"]:
    lb.insert(END, item)
lb.pack()
root.mainloop()