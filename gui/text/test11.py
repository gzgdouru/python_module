#coding:utf8
'''
11.使用indexes获得Text中的内容
'''
from Tkinter import *
root = Tk()
t = Text(root)
for i in range(10):
    t.insert(1.0, "0123456789\n")
#print t.get("1.0", "2.3")
t.mark_set("ab", "1.0")
t.mark_set("cd", END)
print t.get("ab", "cd")
t.pack()
root.mainloop()