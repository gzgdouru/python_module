#coding:utf8
'''
6.设置scale的标签属性label
'''
from Tkinter import *

def printScale(text):
    print text
    print v.get()

root = Tk()
v = StringVar()
Scale(root,
      from_=0,   # 设置最小值
      to=100.0,   # 设置最大值
      resolution=0.0001, # 设置步长
      orient=HORIZONTAL,  #设置水平方向
      digits=8, #设置显示的位数为8
      variable=v,    #绑定变量
      label="choice:", #设置标签值
      command=printScale
      ).pack()
root.mainloop()