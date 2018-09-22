#coding:utf8
'''
2.改变三个参数,生成一个水平scale,最小值-500,最大值500,步距5
'''
from Tkinter import *

root = Tk()
Scale(root,
      from_=-500,   # 设置最小值
      to=500,   # 设置最大值
      resolution=5, # 设置步长
      orient=HORIZONTAL  #设置水平方向
      ).pack()
root.mainloop()