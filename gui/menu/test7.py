#coding:utf8
'''
7.菜单项的操作发放
'''
from Tkinter import *

def printItem():
    print "add_separator"

root = Tk()
menubar = Menu(root)
fileMenubar = Menu(menubar, tearoff=0)
for item in ["python", "php", "c++", "java", "js"]:
    fileMenubar.add_command(label=item, command=printItem)
    #fileMenubar.add_separator() #添加分割符
menubar.add_cascade(label="language", menu=fileMenubar)

fileMenubar.insert_command(1, label="lua", command=printItem)
fileMenubar.insert_command(2, label="c#", command=printItem)
fileMenubar.insert_command(3, label="golang", command=printItem)
#fileMenubar.insert_separator(1)
#fileMenubar.insert_separator(5)

fileMenubar.delete(6, 9)
fileMenubar.delete(0)

root.configure(menu=menubar)
root.mainloop()