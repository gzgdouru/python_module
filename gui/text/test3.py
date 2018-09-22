#coding:utf8
'''
3.使用line.col索引添加内容
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.insert(1.0, "0123456789")
t.insert("2.end", "\n")
t.insert(2.5, "ABCDEFGHIJ")
t.pack()
root.mainloop()