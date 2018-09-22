#coding:utf8
'''
2.向frame中添加widget(部件)
'''
from tkinter import *

root = Tk()
fm = []
for color in ["red", "blue"]:
    fm.append(Frame(height=40, width=400, bg=color))
Label(fm[1], text="hello label").pack()
fm[0].pack()
fm[1].pack()
root.mainloop()