#coding:utf8
'''
5.Checkbutton的值不仅仅是1或0，可以是其他类型的数值，可以通过onvalue和offvalue属性设置Checkbutton的状态值，
如下代码将On设置为'python',Off值设置为'Tkinter'，程序的打印值将不再是0或1，而是'Tkinter’或‘python’
'''
from tkinter import *

def callCheckButton():
    print(v.get())

root = Tk()
v = StringVar()
Checkbutton(root, variable=v, text="checkbutton value", offvalue="tkinter", onvalue="python", command=callCheckButton).pack()
root.mainloop()
