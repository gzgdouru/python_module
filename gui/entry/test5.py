#coding:utf8
'''
5.验证输入的内容是否符合要求
使用validate来输入的内容
使用validate方法来限制输入的内容
这是一个有问题的例子,无法调用validateText回调函数
'''
from Tkinter import *

def validateText(contents):
    print contents
    return contents.isalnum()

root = Tk()
e = StringVar()
entry = Entry(root, validate="key", textvariable=e, validatecommand=validateText)
entry.pack()

root.mainloop()