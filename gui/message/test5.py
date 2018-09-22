#coding:utf8
'''
4.测试justify属性
'''
from Tkinter import *

root = Tk()
for key in [LEFT, RIGHT, CENTER]:
    Message(root, text="ABC DEF GHI", justify=key).pack()
root.mainloop()