#coding:utf8
'''
4.listBox和scrollbar绑定
'''
from Tkinter import *

root = Tk()
lb = Listbox(root)
sl = Scrollbar(root)
sl.configure(command=lb.yview) # 指定scrollbar的回调函数为listbox的yview
sl.pack(side=RIGHT,fill=Y)
for i in range(100):
    lb.insert(END, i)
lb.configure(yscrollcommand=sl.set) # 执行listbox的yscrollbar的回调函数为scrollbar的set
lb.pack(side=LEFT, fill=Y)
root.mainloop()