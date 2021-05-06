import time
import pyautogui
import tkinter as tk


def screenshot():
    name=int(round(time.time()*1000))
    name='{}.png'.format(name)
    img=pyautogui.screenshot(name)
    img.show()
 

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

B = tk.Button(frame,text ="Take Screenshot",fg='green', command = screenshot)

B.pack(side=tk.LEFT)
c=tk.Button(frame,text="quit",fg='red',command=quit)
c.pack(side=tk.LEFT)

root.mainloop()