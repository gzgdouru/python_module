#coding:utf8
'''
2.在entry中设定初始值,使用textvariable将变量与Entry绑定
'''
from Tkinter import *

root = Tk()

e = StringVar()
entry = Entry(root, textvariable=e)
e.set("input your text here")
entry.pack()

root.mainloop()