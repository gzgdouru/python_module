#coding:utf8
'''
6.右键弹出菜单
'''
from Tkinter import *

def printItem():
    print "pop menu"

def pop_menu(event):
    menubar.post(event.x_root, event.y_root)    # 显示菜单

root = Tk()
menubar = Menu(root)
fileMenubar = Menu(menubar, tearoff=0)
for item in ["python", "php", "c++", "java", "js"]:
    fileMenubar.add_command(label=item, command=printItem)
    fileMenubar.add_separator() #添加分割符
menubar.add_cascade(label="language", menu=fileMenubar)
root.configure(menu=menubar)

#在这里相应鼠标的右键事件，右击时调用pop_menu,此时与菜单绑定的是root，可以设置为其它的控件，在绑定的控件上右击就可以弹出菜单
root.bind("<Button-3>", pop_menu)
root.mainloop()