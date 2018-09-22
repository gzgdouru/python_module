#coding:utf8
'''
13.在Text中创建按钮
'''
#from Tkinter import *
from tkinter import *

def printText():
    #print "Button in text"
    print("Button in text")
root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0, "0123456789\n")
bt = Button(t, text="button", command=printText)
t.window_create("2.0", window=bt)
t.pack()
root.mainloop()