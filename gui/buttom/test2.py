#coding:utf8
'''
2.测试Buttom的relief属性
'''

from Tkinter import *

root = Tk()
Button(root, text="hello buttom", relief=FLAT).pack()
Button(root, text="hello buttom", relief=GROOVE).pack()
Button(root, text="hello buttom", relief=RAISED).pack()
Button(root, text="hello buttom", relief=RIDGE).pack()
Button(root, text="hello buttom", relief=SOLID).pack()
Button(root, text="hello buttom", relief=SUNKEN).pack()

root.mainloop()