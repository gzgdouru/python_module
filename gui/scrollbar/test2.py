#coding:utf8
'''
2.通过set方法设置slider的位置
'''
from Tkinter import *

root = Tk()
sl = Scrollbar(root, orient=HORIZONTAL)
sl.set(0.5, 1)
sl.pack()
root.mainloop()