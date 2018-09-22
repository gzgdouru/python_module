#coding:utf8
'''
1.一个简单的Button应用
'''
from Tkinter import *

# 定义buttom回调函数
def helloButtom():
    print "hello Buttom"

root = Tk()
#通过command属性来指定Button的回调函数
Button(root, text="Hello Buttom", command=helloButtom).pack()

root.mainloop()

