import tkinter as tk
from tkinter import messagebox

VALID_USERNAME = 'ARTIN'
VALID_PASSWORD = 1232

def detection():
    username = username_var.get()
    password = password_var.get()
    try:
        if username == VALID_USERNAME and int(password) == VALID_PASSWORD:
            messagebox.showinfo("Authentication", "Authentication successful")
        else:
            messagebox.showinfo("Authentication", "Wrong password or username")
    except ValueError:
        messagebox.showinfo("Authentication", "Password must be a number")

def reset_password():
    new_password = new_password_var.get()
    if new_password:
        global VALID_PASSWORD
        VALID_PASSWORD = int(new_password)
        messagebox.showinfo("Password Reset", "Password has been reset successfully")
    else:
        messagebox.showinfo("Password Reset", "Please enter a new password")

def toggle_remember_me():
    if remember_me_var.get():
        messagebox.showinfo("Remember Me", "You will be remembered")
    else:
        messagebox.showinfo("Remember Me", "You will not be remembered")

# Initialize main window
win = tk.Tk()
win.title("Authentication Form")
win.geometry('400x300')

# Username input
tk.Label(win, text='Username:').pack(pady=5)
username_var = tk.StringVar()
tk.Entry(win, textvariable=username_var).pack(pady=5)

# Password input
tk.Label(win, text='Password:').pack(pady=5)
password_var = tk.StringVar()
tk.Entry(win, textvariable=password_var, show="*").pack(pady=5)

# Submit button
tk.Button(win, text='Submit', command=detection).pack(pady=5)

# Password reset
tk.Label(win, text='Reset Password:').pack(pady=5)
new_password_var = tk.StringVar()
tk.Entry(win, textvariable=new_password_var, show="*").pack(pady=5)
tk.Button(win, text='Reset Password', command=reset_password).pack(pady=5)

# Remember me checkbox
remember_me_var = tk.BooleanVar()
tk.Checkbutton(win, text='Remember Me', variable=remember_me_var, command=toggle_remember_me).pack(pady=5)

# Run the main loop
win.mainloop()

