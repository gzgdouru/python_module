#coding:utf8
'''
2.向text添加文本内容
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.insert(1.0, "0123456789")
t.insert(1.0, "ABCDEFGHIJ")
t.pack()
root.mainloop()