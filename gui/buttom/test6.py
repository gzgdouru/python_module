#coding:utf8
'''
6.设置Button文本在控件上的显示位置
anchor：使用的值为:n(north),s(south),w(west),e(east)和ne,nw,se,sw，就是地图上的标识位置了，使用width和height属性是为了显示各个属性的不同。
'''
from Tkinter import *

root = Tk()

for key in ["n", "s", "w", "e", "ne", "nw", "se", "sw"]:
    Button(root, text="anchor", anchor=key, width=30, height=4).pack()

root.mainloop()