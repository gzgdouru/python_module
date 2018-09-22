#coding:utf8
'''
7.改变Button的前景色与背景色
fg: 前景色
bg: 背景色
'''

from Tkinter import *

root = Tk()

Button(root, text="change foreground", fg="red").pack()
Button(root, text="change background", bg="blue").pack()

root,mainloop()