#coding:utf8
'''
9.对文件块添加tag
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config("b", foreground="red")
for i in range(10):
    t.insert(1.0, "0123456789\n")
t.tag_add("b", "2.5", "5.end")
t.pack()
root.mainloop()