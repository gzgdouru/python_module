#coding:utf8
'''
3.使用list作为optionMenu的选项
'''
from Tkinter import *

def printItem(event, value):
    print value.get()

root = Tk()
lang = ['Python','PHP','CPP','C','Java','JavaScript','VBScript']
v = StringVar()
v.set("Tkinter")
om = apply(OptionMenu, (root, v) + tuple(lang))
om.bind("<Button-1>", lambda event: printItem(event, v))
om.pack()
root.mainloop()