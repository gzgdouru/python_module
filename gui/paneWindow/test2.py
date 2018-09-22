#coding:utf8
'''
2.删除paneWindow指定pane
'''
from Tkinter import *

root = Tk()
ws = []
panes = PanedWindow(orient=VERTICAL)
panes.pack(fill=BOTH, expand=1)
for key in [Label, Button, Checkbutton, Radiobutton]:
  ws.append(key(panes, text="hello"))
[panes.add(w) for w in ws]
#panes.forget(ws[1])
panes.remove(ws[1])
root.mainloop()