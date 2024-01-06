from tkinter import *
import datetime
import calendar
import pytz
import time



def update():
    time_string = datetime.datetime.now()

    

    time_stringg = f'{time_string.hour}:{time_string.minute}:{time_string.second} {datetime.datetime.now().strftime("%p")}'

    if time_string.minute < 10:
        time_stringg = f'{time_string.hour}:0{time_string.minute}:{time_string.second} {datetime.datetime.now().strftime("%p")}'
    
    if time_string.second < 10:
        time_stringg = f'{time_string.hour}:{time_string.minute}:0{time_string.second} {datetime.datetime.now().strftime("%p")}'

    if time_string.second < 10 and time_string.minute < 10:
        time_stringg = f'{time_string.hour}:0{time_string.minute}:0{time_string.second} {datetime.datetime.now().strftime("%p")}'
    
    
    time_label.config(text=time_stringg)


    day_stringb = datetime.datetime.today()
    day_string = calendar.day_name[day_stringb.weekday()]

    day_label.config(text=day_string)

    date_stringni = datetime.datetime.now().month

    date_stringb = int(date_stringni)

    global dwn
    

    if date_stringb == 1:
        date_string = 'January'

    if date_stringb == 2:
        date_string = 'February'

    if date_stringb == 3:
        date_string = 'March'

    if date_stringb == 4:
        date_string = 'April'

    if date_stringb == 5:
        date_string = 'May'

    if date_stringb == 6:
        date_string = 'June'

    if date_stringb == 7:
        date_string = 'July'

    if date_stringb == 8:
        date_string = 'August'

    if date_stringb == 9:
        date_string = 'September'
    
    if date_stringb == 10:
        date_string = 'October'
    
    if date_stringb == 11:
        date_string = 'November'

    if date_stringb == 12:
        date_string = 'December'
    
    

    date_stringg = f'{date_string} {datetime.datetime.now().day}, {datetime.datetime.now().year}'
    

    date_label.config(text=date_stringg)

    
    screen1.after(1000,update)


screen1 = Tk()

time_label = Label(screen1,font=("Arial",50))
time_label.pack()

Label(screen1,text="______________________________").pack()

day_label = Label(screen1,font=("Ariel",25,"bold"))
day_label.pack()

date_label = Label(screen1,font=(None,30))
date_label.pack()


update()


screen1.mainloop()