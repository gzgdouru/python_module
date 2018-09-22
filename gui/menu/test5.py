#coding:utf8
'''
5.向菜单中添加分隔符
'''
from Tkinter import *

def printItem():
    print "add_separator"

root = Tk()
vlang = StringVar()
menubar = Menu(root)
fileMenubar = Menu(menubar, tearoff=0)
for item in ["python", "php", "c++", "java", "js"]:
    fileMenubar.add_command(label=item, command=printItem)
    fileMenubar.add_separator() #添加分割符
menubar.add_cascade(label="language", menu=fileMenubar)
root.configure(menu=menubar)
root.mainloop()