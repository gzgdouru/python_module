#coding:utf8
'''
3.scale绑定变量
'''
from Tkinter import *

root = Tk()
v = StringVar()
Scale(root,
      from_=0,   # 设置最小值
      to=100.0,   # 设置最大值
      resolution=0.0001, # 设置步长
      orient=HORIZONTAL,  #设置水平方向
      variable=v    #绑定变量
      ).pack()
print v.get()
root.mainloop()