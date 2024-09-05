from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

root = Tk()
root.geometry("380x260+500+200")
root.title("Калькулятор")
bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2", ]
r = 5
c = 0



color1="#8000ff"
ttk.Style().configure(".",  font="helvetica 15 ",  padding=8, background=color1, bg=color1)

Label(text="Поле для ввода чисел: ",font="helvetica 14").grid(row=0, column=0,columnspan=5 )

calc_entry = Entry(root, width = 33, font="helvetica 15") # поле ввода
calc_entry.grid(row=1, column=0, columnspan=5)
for i in bttn_list:  #рисуем кнопки
    rel = ""
    cmd=lambda x=i: calc(x)
    if isinstance(i,int):
        color1="#004D40"
    else:
        color1="#8000ff"
    ttk.Button(root, text=i, command=cmd, width=5).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1



#логика калькулятора
def calc(key):
    global memory
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Первый символ не число!")
            messagebox.showerror("Error!", "Вы ввели не число!")
#Вычисление
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Проверьте выражение")
            # очистка поля ввода
    elif key == "C":
         calc_entry.delete(0, END)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key in ("sin", "cos", "n!", "√2"):
        exept_key(key)

    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")


    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
def exept_key(key):
    '''
    проверка на ошибки для "sin" ,"cos", "n!","√2"

    '''
    try:
        if key == "cos":
            result = math.cos(int(calc_entry.get()))
        elif key == "sin":
            result = math.sin(int(calc_entry.get()))
        elif key == "n!":
            result = math.factorial(int(calc_entry.get()))
        elif key == "√2":
            result = math.sqrt(int(calc_entry.get()))
        calc_entry.insert(END, "=" + str(result))
    except:
        calc_entry.insert(END, "Error!")
        messagebox.showerror("Ошибка!", "Для вычисления введите целое число")


root.mainloop()