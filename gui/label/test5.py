#coding:utf8
'''
5.同时使用图像和文本
compound: 指定文本(text)与图像(bitmap/image)是如何在Label上显示,缺省为None
    当指定image/bitmap时,文本(text)将被覆盖,只显示图像,可以使用的值:
    left: 图像居左
    right: 图像居右
    top: 图像居上
    bottom: 图像居下
    center: 文字覆盖在图像上
    bitmap/image: 显示在Label上的图像
    text: 显示在Label上的文本
'''
from Tkinter import *

root = Tk()

Label(root, text="botton", compound="bottom", bitmap="error").pack()
Label(root, text="top", compound="top", bitmap="error").pack()
Label(root, text="right", compound="right", bitmap="error").pack()
Label(root, text="left", compound="left", bitmap="error").pack()
Label(root, text="center", compound="center", bitmap="error").pack()

root.mainloop()