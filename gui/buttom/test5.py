#coding:utf8
'''
5.指定Button的宽度与高度
width: 宽度
height: 高度
使用三中方法"
1.创建Button对象时,指定宽度和高度
2.使用属性wigth 和 heigth 来指定宽度和高度
3.使用configure方法来指定宽度与高度
'''

from Tkinter import *

root = Tk()
Button(root, text="30x1", width=30, height=2).pack()

b2 = Button(root, text="30x2")
b2["width"] = 30
b2["height"] = 3
b2.pack()

b3 = Button(root)
b3.configure(width=30, height=3,text="30x3")
b3.pack()

root.mainloop()


