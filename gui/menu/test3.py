#coding:utf8
'''
3.向菜单添加checkbutton项
'''
from Tkinter import *

def printItem():
    print "python =", vPython.get()
    print "php =", vPhp.get()
    print "c++ =", vC.get()
    print "java =", vJava.get()
    print "js = ", vJs.get()

root = Tk()
menubar = Menu(root)

vPython = StringVar()
vPhp = StringVar()
vC = StringVar()
vJava = StringVar()
vJs = StringVar()

language = {
    "python" : vPython,
    "php" : vPhp,
    "c++" : vC,
    "java" : vJava,
    "js" : vJs
}

fileMenubar = Menu(menubar, tearoff=0)
for key, value in language.items():
    fileMenubar.add_checkbutton(label=key, command=printItem, variable=value)
menubar.add_cascade(label="language", menu=fileMenubar)
root.configure(menu=menubar)
root.mainloop()