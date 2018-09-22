#coding:utf8
'''
1.向paneWindow(面板)中添加pane
'''
from Tkinter import *

root = Tk()
panes = PanedWindow(orient=VERTICAL)
panes.pack(fill=BOTH, expand=1)
for key in [Label, Button, Checkbutton, Radiobutton]:
    panes.add(key(panes, text="hello"))
root.mainloop()