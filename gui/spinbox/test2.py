#coding:utf8
'''
2.设置spinbox的最大,最小值和步长
'''
from Tkinter import *

root = Tk()
Spinbox(root,
        from_=0, #最小值
        to=100, #最大值
        increment=5 #步长值为5
        ).pack()
root.mainloop()