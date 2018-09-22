#coding:utf8
'''
7.同时使用两个文本指定同一个属性
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config("a", foreground="red") #创建一个TAG，其前景色为红色
t.tag_config("b", foreground="blue")
t.insert(1.0, "0123456789", ("b","a")) #使用TAG 'a'来指定文本属性

t.pack()
root.mainloop()