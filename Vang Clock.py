from tkinter import *
from tkinter.ttk import *
from time import strftime

top=Tk()
top.title("Digital Clock")
def none():
    text=strftime(' %H:%m:%S %p ')
    lbl.config(text=text)
    lbl.after(1000,none)
lbl=Label(top,font=('digital-7' ,50, 'bold'),
          background='black' ,foreground='white')
lbl.pack(anchor='center')
none()
mainloop()
