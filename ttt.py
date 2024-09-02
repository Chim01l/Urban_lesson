from tkinter import *
window1 = Tk()

def fun1():
    check1 = IntVar()
    checkbox1 = Checkbutton(window1, variable=check1, text="Что-то там")
    checkbox1.grid(row=1, column=0)
    checkbox1.select()


fun1()

check2 = IntVar()
checkbox2 = Checkbutton(window1, variable=check2, text="Что-то там")
checkbox2.grid(row=3, column=0)
checkbox2.select()


window1.mainloop()