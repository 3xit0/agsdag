# -*- coding: cp1251 -*-

from tkinter import *
import Converter

def Convert():
    N = entryfield.get()
    result.configure(text=Converter.Main(N))

window = Tk()

window.title('Converter')
window.geometry('300x200')

help = Label(window, text='Write a number here!', font=150)
help.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.14)

result = Label(window, text='There will be the result:', font=150)
result.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.14)

entryfield = Entry(window, width=23, bg='#E4E4E4', font=150)
entryfield.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.14)

button = Button(window, text='Convert', font=150, command=lambda:Convert())
button.place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.14)

window.resizable(False, False)

window.mainloop()