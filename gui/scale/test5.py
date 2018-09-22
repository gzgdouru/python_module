#coding:utf8
'''
5.控制显示位数,可以理解为:scale的值为一组整形,在输出显示时,它将会被转化为一字符串,如1.2转化为1.2或者1.2000都是可以的
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
      command=printScale
      ).pack()
root.mainloop()