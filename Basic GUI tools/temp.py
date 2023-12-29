import tkinter as tk

def convert_temperature():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"Result: {fahrenheit}°F")

root = tk.Tk()
root.title("Temperature Converter")

entry = tk.Entry(root)
entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

root.mainloop()
