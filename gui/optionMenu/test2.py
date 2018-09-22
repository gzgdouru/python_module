#coding:utf8
'''
2.打印optionMenu的值
'''
from Tkinter import *

def printItem(event, value):
    print value.get()

root = Tk()
v = StringVar()
v.set("Tkinter")
om = OptionMenu(root, v, 'Python','PHP','CPP','C','Java','JavaScript','VBScript')
om.bind("<Button-1>", lambda event: printItem(event, v))
om.pack()
root.mainloop()