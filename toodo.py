import tkinter as tk
from tkinter import messagebox
def add_task():
    tasks_entry.get()
    if tasks_entry:
        tasks.append(tasks_entry)
        task_listbase(tk.END,tasks_entry)
        tasks_entry.insert(tk.END)
        tasks_entry.delete(tk.END)
def delete():
    try:
       selected_tasks_inbox=task_listbase.cursorselection()[0] 
       task_listbase.delete(selected_tasks_inbox)
       tasks.pop(selected_tasks_inbox)
    except IndexError:
        messagebox.showinfo('please select a task')
        
roo=tk.Tk()
delete_button=tk.Button(roo,text='delete task').pack()
roo.title('todo-list')
tasks=[]
tasks_entry=tk.Entry(roo,width=50).pack()
roo.geometry('800x600')
button=tk.Button(roo,text='add task',command=add_task).pack(pady=5)
task_listbase=tk.Listbox(roo,width=50).pack(pady=10)
roo.mainloop()