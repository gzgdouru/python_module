#coding:utf8
'''
3.LabelFrame添加了title的支持
'''
from tkinter import *

root = Tk()
fm = []
for color in ["red", "blue", "yellow"]:
    LabelFrame(height=40, width=400, text=color).pack()
root.mainloop()