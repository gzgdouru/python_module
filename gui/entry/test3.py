#coding:utf8
'''
3.设置制度entry
'''
from Tkinter import *

root = Tk()

e = StringVar()
enrty = Entry(root, textvariable=e)
e.set("input your text here")
enrty.configure(state="readonly")
enrty.pack()

root.mainloop()