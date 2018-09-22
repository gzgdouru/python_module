#coding:utf8
'''
2.添加下拉菜单
'''
from Tkinter import *

def hello():
    print "hello menu"

root = Tk()
menubar = Menu(root)
fileMenubar = Menu(menubar, tearoff=0)
for item in ["python", "php", "c++", "java", "js"]:
    fileMenubar.add_command(label=item, command=hello)
menubar.add_cascade(label="language", menu=fileMenubar)
root.configure(menu=menubar)
root.mainloop()