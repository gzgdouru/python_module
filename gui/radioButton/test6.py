#coding:utf8
'''
6.Radiobutton另一个比较实用的属性是indicatoron,缺省情况下为1，如果将这个属性改为0，则其外观是Sunken
'''
from Tkinter import *

root = Tk()
v = IntVar()
v.set(1)
for i in range(3):
    Radiobutton(root, variable=v, indicatoron=0, text="python & tkinter", value=i).pack()

root.mainloop()