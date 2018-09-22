#coding:utf8
'''
1.创建一个简单的menu
'''
from Tkinter import *

def hello():
    print "hello menu"

root = Tk()
menubar = Menu(root)
for item in ["python", "php", "c++", "java", "js"]:
    menubar.add_command(label=item, command=hello)
root.configure(menu=menubar)
root.mainloop()