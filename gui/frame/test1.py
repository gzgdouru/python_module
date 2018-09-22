#coding:utf8
'''
1.创建Frame
'''
from tkinter import *

root = Tk()
for fm in ["red", "blue", "yellow", "green", "white", "black"]:
    Frame(height=40, width=400, bg=fm).pack()
root.mainloop()