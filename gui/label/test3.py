#coding:utf8
'''
3.改变控件前景色和背景色
fg:前景色
bg:背景色
'''
from Tkinter import *

root = Tk()
Label(root, fg="red", bg="blue", text="hello Tkinter").pack()
Label(root, fg="red", bg="#FF00FF", text="hello Tkinter").pack()
root,mainloop()