#coding:utf8
'''
1.创建optionMenu
'''
from Tkinter import *
root = Tk()
v = StringVar()
v.set("python")
OptionMenu(root, v, 'Python','PHP','CPP','C','Java','JavaScript','VBScript').pack()
print v.get()
root.mainloop()