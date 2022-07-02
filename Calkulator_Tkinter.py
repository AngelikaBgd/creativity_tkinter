# Main window

import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0':
        value = value[1:]

    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + str(digit))
    calc['state'] = tk.DISABLED


def add_operation(operation):
    value = calc.get()
    if value[-1] in '*/+-':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    try:
        result = eval(value)
        if result == 0.0:
            result = 0
        calc.insert(0, result)
        calc['state'] = tk.DISABLED
    except (NameError, SyntaxError):
        messagebox.showinfo("Attention", "Please use only digits and operations!!!")
        calc.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo("Attention!", "Cannot divide by zero.")


def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def button_maker(digit):
    return tk.Button(win, text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def button_operation(operation):
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13),
                     fg='red', command=lambda: add_operation(operation))


def button_calc(command):
    return tk.Button(win, text=command, bd=5, font=('Arial', 13),
                     fg='red', command=calculate)


def button_clear(command):
    return tk.Button(win, text=command, bd=5, font=('Arial', 13),
                     fg='red', command=clear)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == 'c':
        clear()


win = tk.Tk()

win['bg'] = '#33ffe6'
win.title('Calculator')
win.geometry("245x350+10+10")  # Size of screen and screen position +10+10

#Press key
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15, bd=6, fg='black', state=tk.DISABLED, disabledbackground='white')
calc['state'] = tk.NORMAL
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc['font'] = ('Times New Roman', 15)
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=3, pady=3)

# Button digits
button_maker(1).grid(row=2, column=0, stick='wens', padx=3, pady=3)
button_maker(2).grid(row=2, column=1, stick='wens', padx=3, pady=3)
button_maker(3).grid(row=2, column=2, stick='wens', padx=3, pady=3)
button_maker(4).grid(row=3, column=0, stick='wens', padx=3, pady=3)
button_maker(5).grid(row=3, column=1, stick='wens', padx=3, pady=3)
button_maker(6).grid(row=3, column=2, stick='wens', padx=3, pady=3)
button_maker(7).grid(row=4, column=0, stick='wens', padx=3, pady=3)
button_maker(8).grid(row=4, column=1, stick='wens', padx=3, pady=3)
button_maker(9).grid(row=4, column=2, stick='wens', padx=3, pady=3)
button_maker(0).grid(row=5, column=0, stick='wens', padx=3, pady=3)
button_maker('.').grid(row=5, column=1, stick='wens', padx=3, pady=3)

# Button operation
button_operation('+').grid(row=2, column=3, stick='wens', padx=3, pady=3)
button_operation('-').grid(row=3, column=3, stick='wens', padx=3, pady=3)
button_operation('*').grid(row=4, column=3, stick='wens', padx=3, pady=3)
button_operation('/').grid(row=5, column=3, stick='wens', padx=3, pady=3)

button_calc('=').grid(row=5, column=2, stick='wens', padx=3, pady=3)
button_clear('C').grid(row=1, column=0, stick='wens', padx=3, pady=3)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.grid_rowconfigure(5, minsize=60)

win.mainloop()
