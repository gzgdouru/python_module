#coding:utf8
'''
3.这个属性selectmode还可以设置为BROWSE,可以通过鼠标来移动Listbox中的选中位置（不是移动item），这个属性也是Listbox
在默认设置的值，这个程序与1.程序运行的结果的一样的
'''
from Tkinter import *

root = Tk()
lb = Listbox(root, selectmode=BROWSE)
for item in ["python", "tkinter", "widget"]:
    lb.insert(END, item)
lb.pack()
root.mainloop()

# 与BROWSE相似的为SINGLE，但不支持鼠标移动选中位置。
