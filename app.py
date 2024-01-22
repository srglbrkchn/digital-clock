from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_lable.config(text=time_string)
    time_lable.after(1000, update)
window = Tk()

time_lable = Label(window, font=("Roboto-Black", 50), fg="#00FF00", bg="black")
time_lable.pack()

update()



window.mainloop()