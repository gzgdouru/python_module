#coding:utf8
'''
9.设置Button的风格
relief/raised/sunken/groove/ridge
'''
from Tkinter import *

root = Tk()

for r in ["raised", "sunken", "groove", "ridge"]:
    Button(root, text=r, relief=r, width=30).pack()

root.mainloop()