#coding:utf8
'''
3.在paneWindow指定位置添加一个pane
'''
from Tkinter import *

root = Tk()
ws = []
panes = PanedWindow(orient=VERTICAL)
panes.pack(fill=BOTH, expand=1)
for key in [Label, Button, Checkbutton, Radiobutton]:
  ws.append(key(panes, text="hello"))
[panes.add(w) for w in ws]
panes.paneconfig(Label(panes, text="word"), after=ws[0])
root.mainloop()