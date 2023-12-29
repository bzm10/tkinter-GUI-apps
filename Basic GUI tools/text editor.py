import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()
        text.delete(1.0, tk.END)
        text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as file:
        content = text.get(1.0, tk.END)
        file.write(content)

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()
