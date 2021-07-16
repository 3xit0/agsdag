# -*- coding: cp1251 -*-

from tkinter import *
def Main(N):
    try:
        result.configure(text=ATR(N))
    except:
        result.configure(text=RTA(N))

def ATR(A):
    A = int(A)
    if A < 1 or A > 4000:
        return False
    else:
        pass
    R = 'I' * A
    R = R.replace('IIIII', 'V')
    R = R.replace('VV', 'X')
    R = R.replace('XXXXX', 'L')
    R = R.replace('LL', 'C')
    R = R.replace('CCCCC', 'D')
    R = R.replace('DD', 'M')
    R = R.replace('VIIII', 'IX')
    R = R.replace('LXXXX', 'XC')
    R = R.replace('DCCCC', 'CM')
    R = R.replace('IIII', 'IV')
    R = R.replace('XXXX', 'XL')
    R = R.replace('CCCC', 'CD')
    return R

def RTA(R):
  d = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
  n = [d[i] for i in R.lower() if i in d]
  return sum([i if i>=n[min(j+1, len(n)-1)] else -i for j,i in enumerate(n)])

window = Tk()

window.title('Converter')
window.geometry('300x200')

help = Label(window, text='Write a number here!', font=150)
help.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.14)

result = Label(window, text='There will be the result:', font=150)
result.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.14)

entryfield = Entry(window, width=23, bg='#E4E4E4', font=150)
entryfield.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.14)

button = Button(window, text='Convert', font=150, command=lambda:Main(entryfield.get()))
button.place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.14)

window.resizable(False, False)

window.mainloop()