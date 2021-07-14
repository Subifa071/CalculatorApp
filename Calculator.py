from tkinter import *

cal= Tk()
cal.title("Calculator")

expression = ""
cal.iconbitmap('E:\calculator.ico')
cal.config(bg="gray25")


def add(value):
    global expression
    expression += value
    label_display.config(text=expression)

def clear():
    global expression
    expression = ""
    label_display.config(text=expression)


def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_display.config(text=result)


label_display = Label(cal,width=13,borderwidth=5,text="",font=('ds-digital',15,'bold'),bg="gray25",fg="khaki1")
label_display.grid(row=0, column=0, columnspan=4)

button_1 = Button(cal,width=3, text="1", font=('ds-digital',15,'bold'),bg="gray75", command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = Button(cal,width=3, text="2", font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = Button(cal,width=3, text="3", font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_divide = Button(cal,width=3, text="/",font=('ds-digital',15,'bold'),bg="orange2",fg="white",command=lambda: add("/"))
button_divide.grid(row=1, column=3)

button_4 = Button(cal,width=3, text="4",font=('ds-digital',15,'bold'),bg="gray75", command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = Button(cal,width=3, text="5",font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = Button(cal,width=3, text="6",font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = Button(cal,width=3,text="*",font=('ds-digital',15,'bold'),bg="orange2",fg="white", command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

button_7 = Button(cal,width=3, text="7", font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = Button(cal,width=3,text="8", font=('ds-digital',15,'bold'),bg="gray75", command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = Button(cal,width=3, text="9", font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_subtract = Button(cal,width=3, text="-",font=('ds-digital',15,'bold'),bg="orange2",fg="white",command=lambda: add("-"))
button_subtract.grid(row=3, column=3)

button_clear = Button(cal,width=3, text="C",font=('ds-digital',15,'bold'),bg="orange2",fg="white",command=lambda: clear())
button_clear.grid(row=4, column=0)

button_0 = Button(cal,width=3, text="0", font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = Button(cal,width=3, text=".", font=('ds-digital',15,'bold'),bg="gray75",command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_add = Button(cal,width=3, text="+",font=('ds-digital',15,'bold'),bg="orange2",fg="white", command=lambda: add("+"))
button_add.grid(row=4, column=3)

button_equals = Button(cal, text="=", width=22, command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)

mainloop()