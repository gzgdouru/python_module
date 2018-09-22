#coding:utf8
'''
2.设置checkButton的回调函数
'''
from tkinter import *

def callCheckButton():
    print("you check this button")

root = Tk()
Checkbutton(root, text="check pyton", command=callCheckButton).pack()
Checkbutton(root, text="check c++", command=callCheckButton).pack()
root.mainloop()