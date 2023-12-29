import tkinter as tk

def calculate():
    expression = entry.get()
    result = eval(expression)
    result_label.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

root.mainloop()
