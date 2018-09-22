#coding:utf8
'''
3.使用toplevel自己制作提示框
'''
from Tkinter import *

mbYes,mbYesNo,mbYesNoCancel,mbYesNoAbort =0,1,2,4
def messageBox():
    mbType = mbYesNo
    textShow = "yes"
    if mbType == mbYes:
        textShow = "yes"
    elif mbType == mbYesNo:
        textShow = "yes/no"
    elif mbType == mbYesNoCancel:
        textShow = "YesNoCancel"
    elif mbType == mbYesNoAbort:
        textShow = "YesNoAbort"
    tl = Toplevel(width=200, height=400)
    Label(tl, text=textShow).pack()

root = Tk()
Button(root, text="click me", command=messageBox).pack()
root.mainloop()