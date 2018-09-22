#coding:utf8
'''
2.显示不换行,指定足够大的宽度
'''
from Tkinter import *

root = Tk()
Message(root, text="hello message", width=100).pack()
root.mainloop()