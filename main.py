from threading import currentThread
from tkinter import *
from numpy import full
import time

root=Tk()
root.title("MyCalc")
root.iconbitmap("Calc.ico")
root.configure(background="grey")


entry_field = Entry(root, width=35, borderwidth=5 )
entry_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

resFl = BooleanVar()
current_num = StringVar()
full_operation = StringVar()
clr_type = StringVar()
clr_type = "C"
full_operation = ""

def change_btnClr_width():
    if btnClr["text"] == "CE":
        btnClr.config(padx=37)
    if btnClr["text"] == "C":
        btnClr.config(padx=40)

def button_press(num):
    global curent_num
    global resFl
    global full_operation
    global clr_type
    global btnClr
    if resFl == True:
        entry_field.delete(0, END)
        full_operation = ""
        resFl = False
    else:
        pass
    current_num = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current_num) + str(num))
    clr_type = "C"
    btnClr.config(text="C")
    change_btnClr_width()

    return

def op_button_press(sgn):
    global full_operation
    global current_num
    global resFl
    try:
        int(entry_field.get())
        if resFl == True:
            entry_field.delete(0, END)
            resFl = False
        else:
            pass
        current_num = entry_field.get()
        full_operation += current_num + sgn
        entry_field.delete(0, END)
        l=Label(root, text=full_operation).grid(row=7,column=0)
    except:
        err = "Error! (Var)"
        entry_field.delete(0, END)
        entry_field.insert(0, "Error! (Var)")
        entry_field.after(1000, clr_button_press)

def clr_button_press():
    global resFl
    global full_operation
    global clr_type
    if clr_type =="CE":
        entry_field.delete(0, END)
        full_operation = ""
        resFl = False
    else:
        entry_field.delete(0, END)
        clr_type = "CE"
        btnClr.config(text="CE")
        change_btnClr_width()
    return

def sum_button_press():
    global full_operation
    global current_num
    global resFl
    global clr_type
    try:
        int(entry_field.get())
        if resFl == True:
            entry_field.delete(0, END)
            entry_field.insert(0, str(full_operation))
        else:
            resFl = True
            current_num = entry_field.get()
            full_operation += current_num
            full_operation = str(eval(full_operation))
            entry_field.delete(0, END)
            entry_field.insert(0, str(full_operation))
            l=Label(root, text=full_operation).grid(row=7,column=0)
    except:
        err = "Error! (Var)"
        entry_field.delete(0, END)
        entry_field.insert(0, "Error! (Var)")
        entry_field.after(1000, clr_button_press)
    clr_type="CE"
    btnClr.config(text="CE")
    change_btnClr_width()
    return



# Creating buttons
btn1 = Button(root, text="1", padx=40, pady=20, border=2, command=lambda: button_press(1))
btn2 = Button(root, text="2", padx=40, pady=20, border=2, command=lambda: button_press(2))
btn3 = Button(root, text="3", padx=40, pady=20, border=2, command=lambda: button_press(3))

btn4 = Button(root, text="4", padx=40, pady=20, border=2, command=lambda: button_press(4))
btn5 = Button(root, text="5", padx=40, pady=20, border=2, command=lambda: button_press(5))
btn6 = Button(root, text="6", padx=40, pady=20, border=2, command=lambda: button_press(6))

btn7 = Button(root, text="7", padx=40, pady=20, border=2, command=lambda: button_press(7))
btn8 = Button(root, text="8", padx=40, pady=20, border=2, command=lambda: button_press(8))
btn9 = Button(root, text="9", padx=40, pady=20, border=2, command=lambda: button_press(9))

btn0 = Button(root, text="0", padx=40, pady=20, border=2, command=lambda: button_press(0))

btnAdd = Button(root, text="+", padx=40, pady=20, border=2, command=lambda: op_button_press("+"))
btnSub = Button(root, text="-", padx=40, pady=20, border=2, command=lambda: op_button_press("-"))
btnDiv = Button(root, text="*", padx=40, pady=20, border=2, command=lambda: op_button_press("*"))
btnMult = Button(root, text="/", padx=40, pady=20, border=2, command=lambda: op_button_press("/"))

btnEq = Button(root, text="=", padx=40, pady=20, border=2, command=lambda: sum_button_press())

btnClr = Button(root, text="CE", padx=37, pady=20, border=2, command=lambda: clr_button_press())
    
# Showing buttons
btn1.grid(row=3, column=0, padx=3, pady=3)
btn2.grid(row=3, column=1, padx=3, pady=3)
btn3.grid(row=3, column=2, padx=3, pady=3)

btn4.grid(row=2, column=0, padx=3, pady=3)
btn5.grid(row=2, column=1, padx=3, pady=3)
btn6.grid(row=2, column=2, padx=3, pady=3)

btn7.grid(row=1, column=0, padx=3, pady=3)
btn8.grid(row=1, column=1, padx=3, pady=3)
btn9.grid(row=1, column=2, padx=3, pady=3)

btn0.grid(row=4, column=0, padx=3, pady=3, columnspan=3)

btnAdd.grid(row=5, column=0, padx=3, pady=3)
btnSub.grid(row=5, column=1, padx=3, pady=3)

btnMult.grid(row=6, column=0, padx=3, pady=3)
btnDiv.grid(row=6, column=1, padx=3, pady=3)

btnEq.grid(row=5, column=2, padx=3, pady=3)
btnClr.grid(row=6, column=2, padx=3, pady=3)

root.mainloop()