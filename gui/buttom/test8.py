#coding:utf8
'''
8.设置Button边框
bd(bordwidth):缺省为1或2个像素
'''
from Tkinter import *

root = Tk()

for num in range(10):
    Button(root, text=str(num), bd=num).pack()

root.mainloop()