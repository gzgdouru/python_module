#coding:utf8
'''
1.第一个entry程序
'''
from Tkinter import *

root = Tk()

Entry(root, text="input your text here").pack()

root.mainloop()

'''
上面的代码目的是创建一个Entry对象，并在Entry上显示'input your text here',运行此代码，并没有看到文本的显示，由此可知与Lable和
Button不同，Entry的text属性不可以设置Entry的文本 
'''