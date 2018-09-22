#coding:utf8
'''
4.使用内置的mark控制添加位置
INSERT: 光标的插入点
CURRENT: 鼠标的当前位置所对应的字符位置
END: 这个是Text buffer的最后一个字符
SEL_FIRST: 选中文本域的第一个字符,如果没有选中区域则会引发异常
SEL_LAST: 选中文本域的最后一个字符,如果没有选中区域则会引发异常
'''
from Tkinter import *

def insertText():
    t.insert(INSERT, "jcodeer")

def currentText():
    t.insert(CURRENT, "jcodeer")

def endText():
    t.insert(END, "jcodeer")

def selFirstText():
    t.insert(SEL_FIRST, "jcodeer")

def selLastText():
    t.insert(SEL_LAST, "jcodeer")

root = Tk()
t = Text(root)
for i in range(1, 10):
    t.insert(1.0, "0123456789\n")

Button(root, text="insert jcodeer at INSERT", command=insertText).pack(fill=X)
Button(root, text="insert jcodeer at CURRENT", command=currentText).pack(fill=X)
Button(root, text="insert jcodeer at END", command=endText).pack(fill=X)
Button(root, text="insert jcodeer at SEL_FIRST", command=selFirstText).pack(fill=X)
Button(root, text="insert jcodeer at SET_LAST", command=selLastText).pack(fill=X)

t.pack()
root.mainloop()