#coding:utf8
'''
4.使用回调函数打印当前值
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
      variable=v,    #绑定变量
      command=printScale
      ).pack()
root.mainloop()