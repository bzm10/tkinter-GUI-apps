from tkinter import *
import datetime
import calendar
import time

def update():
    current_time = datetime.datetime.now()
    time_format = "%I:%M:%S %p"

    time_label.config(text=current_time.strftime(time_format))
    day_label.config(text=calendar.day_name[current_time.weekday()])
    date_label.config(text=current_time.strftime("%B %d, %Y"))
    root.after(1000, update)  # Schedule the next update after 1000 milliseconds (1 second)

root = Tk()
root.title("Clock App")

time_label = Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
time_label.pack()

day_label = Label(root, font=('calibri', 20, 'bold'), background='black', foreground='white')
day_label.pack()

date_label = Label(root, font=('calibri', 20, 'bold'), background='black', foreground='white')
date_label.pack()

update()

root.mainloop()
