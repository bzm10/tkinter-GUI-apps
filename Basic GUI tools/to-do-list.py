import tkinter as tk

def add_task():
    task = entry.get()
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack(pady=10)

root.mainloop()
