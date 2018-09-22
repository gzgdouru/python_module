#coding:utf8
'''
4.设置宽度和高度
width: 宽度
height: 高度
'''
from Tkinter import *

root = Tk()

Label(root, fg="red", bg="red").pack()
Label(root, fg="blue", bg="blue").pack()
Label(root, fg="yellow", bg="yellow").pack()

Label(root, fg="red", bg="red", width=10, height=3).pack()
Label(root, fg="blue", bg="blue", width=10, height=3).pack()
Label(root, fg="yellow", bg="yellow", width=10, height=3).pack()

root.mainloop()