#coding:utf8
'''
4.向菜单添加Radiobutton项
'''
from Tkinter import *

def printItem(item):
    print "language =", item.get()

root = Tk()
vlang = StringVar()
menubar = Menu(root)
fileMenubar = Menu(menubar, tearoff=0)
for item in ["python", "php", "c++", "java", "js"]:
    fileMenubar.add_radiobutton(label=item, command=lambda:printItem(vlang), variable=vlang)
menubar.add_cascade(label="language", menu=fileMenubar)
root.configure(menu=menubar)
root.mainloop()