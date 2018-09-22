#coding:utf8
'''
3.使用回调函数
'''
from Tkinter import *

def scorllCall(moveto, pos):
    sl.set(pos, 0)
    print sl.get()

root = Tk()
sl = Scrollbar(root, orient=HORIZONTAL, command=scorllCall)
sl.pack()
root.mainloop()