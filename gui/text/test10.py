#coding:utf8
'''
10.使用自定义mark对文本块添加tag
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config("b", foreground="red")
for i in range(10):
    t.insert(1.0, "0123456789\n")
t.mark_set("a", "3.1")
t.mark_set("c", END)
t.tag_add("b", "a", "c")
t.pack()
root.mainloop()