#coding:utf8
'''
3.与Label一样,Button也可以同时显示文本与图像,使用属性compound
'''

from  Tkinter import *

root = Tk()

Button(root, text="bottom", compound="bottom", bitmap="error").pack()
Button(root, text="left", compound="left", bitmap="error").pack()
Button(root, text="right", compound="right", bitmap="error").pack()
Button(root, text="top", compound="top", bitmap="error").pack()
Button(root, text="center", compound="center", bitmap="error").pack()

root.mainloop()