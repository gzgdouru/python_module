#coding:utf8
'''
3.控件焦点问题
'''
from Tkinter import *

def cb1():
    print "button1 clicked"

def cb2(event):
    print "button2 clicked"

def cb3():
    print "button3 clicked"

root = Tk()

b1 = Button(root, text="Button1", command=cb1)
b2 = Button(root, text="Button2")
b2.bind("<Return>", cb2)
b3 = Button(root, text="Button3", command=cb3)

b1.pack()
b2.pack()
b3.pack()

b2.focus_set()

'''
上例中使用了bind方法，它建立事件与回调函数(响应函数）之间的关系，每当产生<Enter>事件后，程序便自动的调用cb2，与cb1,cb3不同的是，
它本身还带有一个参数----event,这个参数传递响应事件的信息。
'''

def printEventInfo(event):
    print "event.time = ", event.time
    print "event.type = ", event.type
    print "event.widgetid = ", event.widget
    print "event,keysymbol = ", event.keysym

b = Button(root, text="Infomation")
b.bind("<Enter>", printEventInfo)
b.pack()
b.focus_set()

'''
犯了个错误，将<Return>写成<Enter>了，结果是：当鼠标进入Button区域后，事件printEventInfo被调用。
程序打印出了event的信息。
'''

root.mainloop()