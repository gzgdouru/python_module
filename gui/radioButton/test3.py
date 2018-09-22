#coding:utf8
'''
3.创建两个不同的组
'''
from Tkinter import *

root = Tk()

vLang = IntVar()
vOs = IntVar()
vLang.set(1)
vOs.set(2)

for j in [vLang, vOs]:
    for i in range(3):
        Radiobutton(root, variable=j, value=i, text="python" + str(i)).pack()

root.mainloop()