#coding:utf8
'''
12.自定义tag的两个内置属性
tag.first:tag之前插入文本，此文本不包含在这个tag中
tag.last:tag之后插入文本，此文本包含在这个tag中
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config("color", foreground="blue")
for i in range(10):
    t.insert(1.0, "0123456789\n")
t.mark_set("ab", "3.1")
t.mark_set("cd", END)
t.tag_add("color", "ab", "cd")
t.insert("color.first", "first")
t.insert("color.last", "last")
t.pack()
root.mainloop()