#coding:utf8
'''
6.设置/取得sacle的值
'''
from Tkinter import *

def printScale(text):
    print text
    print sl.get()

root = Tk()
sl = Scale(root, command=printScale)
sl.set(50)
sl.pack()
root.mainloop()