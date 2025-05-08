import tkinter as tk
from tkinter import messagebox
def messagec_info():
   messagebox.showinfo('info') 
base=tk.Tk()
base.title('message box')
base.geometry('800x600')
menu=tk.Menu(base)
base.config(menu=menu)
submenu=tk.Menu(menu,tearoff=0)
submenu.add_command(label='about us',command=messagec_info)
menu.add_cascade(label='hint',menu=submenu)
frame=tk.Frame(base,relief='solid',borderwidth='2').pack(padx='20',pady='20')
tk.Label(frame,text='click me').pack()
base.mainloop()
