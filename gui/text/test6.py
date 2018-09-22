#coding:utf8
'''
6.使用tag来指定文本的属性
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config("a", foreground="red") #创建一个TAG，其前景色为红色
t.insert(1.0, "0123456789", "a") #使用TAG 'a'来指定文本属性

t.pack()
root.mainloop()