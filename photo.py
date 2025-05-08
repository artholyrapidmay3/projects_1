import tkinter as tk
from PIL import Image,ImageTk
win=tk.Tk()
win.title("show image")
image=Image.open('images/error.png')
image=image.resize((400,300))
photo=ImageTk.PhotoImage(image)
label=tk.Label(win,image=photo)
label.pack()


win.mainloop()