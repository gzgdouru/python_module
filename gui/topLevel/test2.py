#coding:utf8
'''
2.设置toplevel属性
title:设置标题
geometry:设置宽和高
'''
from Tkinter import *

root = Tk()
tl = Toplevel()
tl.title("hello toplevel")
tl.geometry("400x300")
Label(tl, text="hello label").pack()
root.mainloop()