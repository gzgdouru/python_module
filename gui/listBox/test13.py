#coding:utf8
'''
13.Listbox与事件绑定
'''
from Tkinter import *

def printList(event):
    print lb.get(lb.curselection())

root = Tk()
v = StringVar()
lb = Listbox(root)
lb.bind("<Double-Button-1>", printList)
for i in range(10):
    lb.insert(END, str(i*100))
lb.pack()
root.mainloop()