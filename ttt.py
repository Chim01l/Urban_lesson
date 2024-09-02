from tkinter import *
window1 = Tk()

def fun1():
    check1 = IntVar()
    check1 = True
    checkbox1 = Checkbutton(window1, variable=check1, text="Что-то там")
    checkbox1.grid(row=1, column=0)
    checkbox1.select()
    check2 = IntVar()
    check2 = True
    checkbox2 = Checkbutton(window1, variable=check2, text="Другой текст")
    checkbox2.grid(row=3, column=0)
    checkbox2.select()


fun1()

window1.mainloop()
