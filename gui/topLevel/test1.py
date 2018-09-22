#coding:utf8
'''
1.创建简单的toplevel
'''
from Tkinter import *

root = Tk()
tl = Toplevel()
Label(tl, text="hello label").pack()
root.mainloop()