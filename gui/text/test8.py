#coding:utf8
'''
8.控制tag的级别
'''
from Tkinter import *
root = Tk()
t = Text(root)
t.tag_config("a", foreground="red") #创建一个TAG，其前景色为红色
t.tag_config("b", foreground="blue")
t.tag_lower("b")    # 降低b的级别
t.insert(1.0, "0123456789", ("b","a")) #使用TAG来指定文本属性

t.pack()
root.mainloop()