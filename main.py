from threading import currentThread
from tkinter import *
from tkinter import font
from numpy import full, sign, test
import time
import keyboard

root=Tk()
root.title("MyCalc")
root.iconbitmap("Calc.ico")
root.configure(background="#383F45")


resFl = BooleanVar()
current_num = StringVar()
full_operation = StringVar()
full_operation = ""
clr_type = StringVar()
clr_type = "C"
sgnFl = BooleanVar()
sgnFl = False
commaFl = BooleanVar()
commaFl = False


def button_press(num):
    global curent_num
    global resFl
    global full_operation
    global clr_type
    global btnClr
    global sgnFl
    if resFl == True:
        full_operation_label.config(text="")
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
    full_operation_label.config(text=full_operation)
    sgnFl = False
    return

def op_button_press(sgn):
    global full_operation
    global current_num
    global resFl
    global sgnFl
    if resFl == True:
        entry_field.delete(0, END)
        resFl = False
    else:
        pass
    if sgnFl == False:
        current_num = entry_field.get()
        full_operation += current_num + sgn
        entry_field.delete(0, END)
        full_operation_label.config(text=full_operation)
        sgnFl = True
    else:
        full_operation = full_operation[:-1]
        full_operation += sgn
        entry_field.delete(0, END)
        full_operation_label.config(text=full_operation)

def clr_button_press():
    global resFl
    global full_operation
    global clr_type
    if clr_type =="CE":
        entry_field.delete(0, END)
        full_operation = ""
        full_operation_label.config(text=full_operation)
        resFl = False
    else:
        entry_field.delete(0, END)
        clr_type = "CE"
        btnClr.config(text="CE")
    return

def sum_button_press():
    global full_operation
    global current_num
    global resFl
    global clr_type
    try:
        if sgnFl == True:
            full_operation = full_operation[:-1]
        if resFl == True:
            entry_field.delete(0, END)
            entry_field.insert(0, str(full_operation))
        else:
            resFl = True
            current_num = entry_field.get()
            full_operation += current_num
            full_operation_label.config(text=full_operation + "=" + str(eval(full_operation)))
            full_operation = str(eval(full_operation))
            entry_field.delete(0, END)
            entry_field.insert(0, str(full_operation))
        clr_type="CE"
        btnClr.config(text="CE")
    except:
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")
    return

def posneg_button_press():
    global entry_field
    entry = entry_field.get()
    if len(entry) > 0:
        if entry[0] != "-":
            entry = "-" + entry
            entry_field.delete(0, END)
            entry_field.insert(0, entry)
        elif entry[0] == "-":
            entry = entry.replace("-", "")
            entry_field.delete(0, END)
            entry_field.insert(0, entry)
    return

def comma_button_press():
    global entry_field
    entry = entry_field.get()
    result = entry.find(".")
    if result == -1:
        commaResFl = False
    else:
        commaResFl = True
    if commaResFl == False:
        if len(entry) > 0:
            entry += "."
            entry_field.delete(0, END)
            entry_field.insert(0, entry)
        elif len(entry) == 0:
            entry_field.insert(0, "0.")
    else:
        pass
    return

# Creating widgets
entry_field = Entry(root, width=65, borderwidth=5)
full_operation_label = Label(root, width=43, borderwidth=5, font=("Heveltica", 11, "bold"), bg="#454C52", fg="white", anchor=E)

btn1 = Button(root, text="1", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(1))
btn2 = Button(root, text="2", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(2))
btn3 = Button(root, text="3", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(3))
keyboard.on_press_key("1", lambda _: button_press(1))
keyboard.on_press_key("2", lambda _: button_press(2))
keyboard.on_press_key("3", lambda _: button_press(3))


btn4 = Button(root, text="4", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(4))
btn5 = Button(root, text="5", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(5))
btn6 = Button(root, text="6", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(6))
keyboard.on_press_key("4", lambda _: button_press(4))
keyboard.on_press_key("5", lambda _: button_press(5))
keyboard.on_press_key("6", lambda _: button_press(6))

btn7 = Button(root, text="7", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(7))
btn8 = Button(root, text="8", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(8))
btn9 = Button(root, text="9", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#52606D", fg="white", command=lambda: button_press(9))
keyboard.on_press_key("7", lambda _: button_press(7))
keyboard.on_press_key("8", lambda _: button_press(8))
keyboard.on_press_key("9", lambda _: button_press(9))

btnPosNeg = Button(root, text="+/-", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: posneg_button_press())
btn0 = Button(root, text="0", width=25, pady=30, border=2, font=("Heveltica", 10, "bold"), bg="#52606D", fg="white", command=lambda: button_press(0))
btnComma = Button(root, text=",", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: comma_button_press())
keyboard.on_press_key("SPACEBAR", lambda _: posneg_button_press())
keyboard.on_press_key("0", lambda _: button_press(0))
keyboard.on_press_key(",", lambda _: comma_button_press())


btnAdd = Button(root, text="+", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: op_button_press("+"))
btnSub = Button(root, text="-", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: op_button_press("-"))
btnMult = Button(root, text="*", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: op_button_press("*"))
btnDiv = Button(root, text="/", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: op_button_press("/"))
keyboard.on_press_key("+", lambda _: op_button_press("+"))
keyboard.on_press_key("-", lambda _: op_button_press("-"))
keyboard.on_press_key("*", lambda _: op_button_press("*"))
keyboard.on_press_key("/", lambda _: op_button_press("/"))


btnEq = Button(root, text="=", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: sum_button_press())
btnClr = Button(root, text="CE", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: clr_button_press())
keyboard.on_press_key("ENTER", lambda _: sum_button_press())
keyboard.on_press_key("ESC", lambda _: clr_button_press())

btnPercent = Button(root, text="%", width=10, height=4, border=2, font=("Heveltica", 11, "bold"), bg="#ffcb2e", command=lambda: sum_button_press())


# Showing widgets
full_operation_label.grid(row=0, column=0, columnspan=4, padx=10, pady=8) #Row 0

entry_field.grid(row=1, column=0, columnspan=4, padx=10, pady=8) #Row 1

btnClr.grid(row=2, column=0, padx=3, pady=3) #Row 2
btnPosNeg.grid(row=2, column=1, padx=3, pady=3)
btnPercent.grid(row=2, column=2, padx=3, pady=3)
btnDiv.grid(row=2, column=3, padx=3, pady=3)  

btn7.grid(row=3, column=0, padx=3, pady=3) #Row 3
btn8.grid(row=3, column=1, padx=3, pady=3) 
btn9.grid(row=3, column=2, padx=3, pady=3)
btnMult.grid(row=3, column=3, padx=3, pady=3)  

btn4.grid(row=4, column=0, padx=3, pady=3) #Row 4
btn5.grid(row=4, column=1, padx=3, pady=3) 
btn6.grid(row=4, column=2, padx=3, pady=3) 
btnSub.grid(row=4, column=3, padx=3, pady=3) 

btn1.grid(row=5, column=0, padx=3, pady=3) #Row 5
btn2.grid(row=5, column=1, padx=3, pady=3) 
btn3.grid(row=5, column=2, padx=3, pady=3)
btnAdd.grid(row=5, column=3, padx=3, pady=3)

btnComma.grid(row=6, column=0, padx=3, pady=3) #Row 6
btn0.grid(row=6, column=1, padx=3, pady=3, columnspan=2) 
btnEq.grid(row=6, column=3, padx=3, pady=3)


root.mainloop()