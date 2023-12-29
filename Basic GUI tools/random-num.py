import tkinter as tk
import random

def generate_number():
    number = random.randint(1, 100)
    result_label.config(text=f"Generated Number: {number}")

root = tk.Tk()
root.title("Random Number Generator")

generate_button = tk.Button(root, text="Generate Number", command=generate_number)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="Generated Number:")
result_label.pack(pady=10)

root.mainloop()
