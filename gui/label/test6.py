#coding:utf8
'''
6.使用width和heigth来指定控件的大小，如果指定的大小无法满足文本的要求
    超出Label的那部分文本被截断了，常用的方法是：使用自动换行功能，及当文本长度大于控件的宽度时，
    文本应该换到下一行显示，Tk不会自动处理，但提供了属性：
    wraplength：指定多少单位后开始换行
    justify: 指定多行的对齐方式
    ahchor：指定文本(text)或图像(bitmap/image)在Label中的显示位置
    可用的值：
    e
    w
    n
    s
    ne
    se
    sw
    sn
    center
    布局如下图
        nw        n        ne
        w     center    e
        sw        s        se

    justify与anchor的区别：一个用于控制多行的对齐；另一个用于控制整个文本块在Label中的位置
'''
from Tkinter import *

root = Tk()

#左对齐，文本居中
Label(root, text="welcome to jcodeer.cublog.cn", bg="yellow", width=40, height=3, wraplength=80, justify="left").pack()

#居中对齐，文本居左
Label(root, text="welcome to jcodeer.cublog.cn", bg="red", width=40, height=3, wraplength=80, anchor="w").pack()

#居中对齐，文本居右
Label(root, text="welcome to jcodeer.cublog.cn", bg="blue", width=40, height=3, wraplength=80, anchor="e").pack()

root,mainloop()