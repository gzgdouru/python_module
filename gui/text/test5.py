#coding:utf8
'''
5.使用表达式来增强mark
+ count chars :前移count字符
- count chars :后移count字符
+ count lines :前移count行
- count lines :后移count行
linestart:移动到行的开始
linesend:移动到行的结束
wordstart:移动到字的开始
wordend:移动到字的结束
'''
from Tkinter import *

def forwardChars():
    #t.mark_set(a, CURRENT+"+ 5 chars")
    t.mark_set(a, CURRENT+"+5c")

def backwardChars():
    t.mark_set(a, CURRENT-"-5c")

def forwardLines():
    #t.mark_set(a, CURRENT+"+ 5 lines")
    t.mark_set(a, CURRENT+"+5l")

def backwardLines():
    t.mark_set(a, CURRENT-"-5l")

def lineStart():
    t.mark_set(a, CURRENT+" linestart")

def lineEnd():
    t.mark_set(a, CURRENT+" lineend")

def wordStart():
    t.mark_set(a, CURRENT+" wordstart")

def wordEnd():
    t.mark_set(a, CURRENT+" wordend")

root = Tk()
t = Text(root)
a = "test_mark"

for i in range(1, 10):
    t.insert(1.0, "0123456789\n")

Button(root, text="forward 5 chars", command=forwardChars).pack(fill=X)
Button(root, text="backward 5 chars", command=backwardChars).pack(fill=X)
Button(root, text="forward 5 lines", command=forwardLines).pack(fill=X)
Button(root, text="backward 5 lines", command=backwardLines).pack(fill=X)
Button(root, text="line start", command=lineStart).pack(fill=X)
Button(root, text="line end", command=lineEnd).pack(fill=X)
Button(root, text="word start", command=wordStart).pack(fill=X)
Button(root, text="word end", command=wordEnd).pack(fill=X)

t.pack()
root.mainloop()