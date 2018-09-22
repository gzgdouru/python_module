#coding:utf8
#2.在label上使用内置位图bitmap的使用方法
from Tkinter import *

root = Tk()
label = Label(root, bitmap="gray50")
label.pack()
root.mainloop()

'''
其他可用的位图：
    * error
    * hourglass
    * info
    * questhead
    * question
    * warning
    * gray12 
    * gray25 
    * gray50
    * gray75
    '''
