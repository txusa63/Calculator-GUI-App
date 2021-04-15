import tkinter as tk
from tkinter import messagebox
from db import Database
from util import *
import decimal
import math
import settings
db = Database('calculator_tape.db')
settings.init()

root = tk.Tk()
root.title('Calculator')
root.geometry("680x350")


def populate_tape():
    tape.delete(0, tk.END)
    for row in db.fetch():
        tape.see(tk.END)
        tape.insert(tk.END, "{} {}".format(row[0], row[1]))
        tape.see(tk.END)


def extract_result(result):
    temp_s = ''
    for i in range(len(result)):
        if i > result.find('='):
            temp_s += result[i]
    e.delete(0, tk.END)
    e.insert(tk.END, str(decimal.Decimal(temp_s)))


def select_item(event):
    try:
        index = tape.curselection()[0]
        selected_item = tape.get(index)
        extract_result(selected_item)

    except IndexError:
        pass


def btn_click(value):
    if e.get().find('=') != -1:
        if value == '+' or value == '-' or value == 'x' or value == '/':
            result = e.get()
            extract_result(result)
        else:
            e.delete(0, tk.END)
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(value))


def all_clear():
    msg = messagebox.askquestion(
        "Warning from Application", "Are you sure you want to delete all values?")
    if msg == 'yes':
        db.remove()
        populate_tape()


def clear():
    e.delete(0, tk.END)


def plus_minus():
    print("num_str = ", e.get())

    if '=' in e.get() and e.get() != '0':
        extract_result(e.get())

    if e.get() != '0' and number_check(e.get()):
        if e.get()[0] != '-':
            e.insert(0, '-')
        else:
            e.delete(0)


def percentage():
    if len(e.get()) != 0 and number_check(e.get()):
        num = int(e.get())
        num = num/100
        e.insert(len(e.get()), '% = ' + str(num))


def delete():
    num_len = len(e.get())
    e.delete(num_len-1)


def square():
    value = e.get()
    if e.get().find('=') != -1:
        extract_result(value)
        e.insert(tk.END, 'x' + e.get())
    elif e.get().find('+') != -1 or e.get().find('x') != -1 or e.get().find('/') != -1:
        temp = ''
        for i in range(len(value)-1, 0, -1):
            print(value[i])
            if value[i] != '+' and value[i] != 'x' and value[i] != '/':
                print("the value is ", value[i])
                temp += value[i]
            else:
                break
        e.delete(0, tk.END)
        value = value + "x" + temp
        e.insert(tk.END, value)

    else:
        value = e.get()
        e.delete(0, tk.END)
        value = value + "x" + value
        e.insert(tk.END, value)


def equals():
    operation = e.get()
    result = 0

    if not check_bad_operators(operation):
        result = filter_numbers(operation)
        result = "".join(str(el) for el in result)
        operation = operation + ' = '

        e.delete(0, tk.END)
        db.insert(operation, str(result))
        e.insert(tk.END, operation + str(result))
        populate_tape()
    else:
        generate_error_message()
        return


# Tape (Listbox)
tape = tk.Listbox(root, height=8, width=60, border=2)
tape.grid(row=0, column=0, columnspan=6, rowspan=1, padx=10, pady=10)

# Create Scrollbar for Tape
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=0, column=6, sticky=tk.N+tk.S+tk.W)

# Set scroll to Listbox
tape.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=tape.yview)

# Bind select
tape.bind('<<ListboxSelect>>', select_item)


e = tk.Entry(root, width=70, borderwidth=5)
e.grid(row=1, column=0, columnspan=6, rowspan=1, padx=10, pady=10)

# Define Calculator Buttons
btn_all_clear = tk.Button(root, text='AC', padx=9,
                          pady=0, width=8, command=all_clear)
btn_all_clear.grid(row=2, column=0)
btn_clear = tk.Button(root, text='C', padx=9, pady=0, width=8, command=clear)
btn_clear.grid(row=2, column=1)
btn_plus_minus = tk.Button(root, text='+/-', padx=9,
                           pady=0, width=8, command=plus_minus)
btn_plus_minus.grid(row=2, column=2)
btn_percentage = tk.Button(root, text='%', padx=9,
                           pady=0, width=8, command=percentage)
btn_percentage.grid(row=2, column=3)
btn_delete = tk.Button(root, text='⌫', padx=9, pady=0, width=8, command=delete)
btn_delete.grid(row=2, column=4)

btn_7 = tk.Button(root, text='7', padx=9, pady=0,
                  width=8, command=lambda: btn_click('7'))
btn_7.grid(row=3, column=0)
btn_8 = tk.Button(root, text='8', padx=9, pady=0,
                  width=8, command=lambda: btn_click('8'))
btn_8.grid(row=3, column=1)
btn_9 = tk.Button(root, text='9', padx=9, pady=0,
                  width=8, command=lambda: btn_click('9'))
btn_9.grid(row=3, column=2)
btn_pi = tk.Button(root, text='π', padx=9, pady=0, width=8,
                   command=lambda: btn_click(str(math.pi)))
btn_pi.grid(row=3, column=3)
btn_square = tk.Button(root, text='X²', padx=9,
                       pady=0, width=8, command=square)
btn_square.grid(row=3, column=4)

btn_4 = tk.Button(root, text='4', padx=9, pady=0,
                  width=8, command=lambda: btn_click('4'))
btn_4.grid(row=4, column=0)
btn_5 = tk.Button(root, text='5', padx=9, pady=0,
                  width=8, command=lambda: btn_click('5'))
btn_5.grid(row=4, column=1)
btn_6 = tk.Button(root, text='6', padx=9, pady=0,
                  width=8, command=lambda: btn_click('6'))
btn_6.grid(row=4, column=2)
btn_division = tk.Button(root, text='/', padx=9, pady=0,
                         width=8, command=lambda: btn_click('/'))
btn_division.grid(row=4, column=3)
btn_multiplication = tk.Button(
    root, text='x', padx=9, pady=0, width=8, command=lambda: btn_click('x'))
btn_multiplication.grid(row=4, column=4)

btn_1 = tk.Button(root, text='1', padx=9, pady=0,
                  width=8, command=lambda: btn_click('1'))
btn_1.grid(row=5, column=0)
btn_2 = tk.Button(root, text='2', padx=9, pady=0,
                  width=8, command=lambda: btn_click('2'))
btn_2.grid(row=5, column=1)
btn_3 = tk.Button(root, text='3', padx=9, pady=0,
                  width=8, command=lambda: btn_click('3'))
btn_3.grid(row=5, column=2)
btn_addition = tk.Button(root, text='+', padx=9, pady=0,
                         width=8, command=lambda: btn_click('+'))
btn_addition.grid(row=5, column=3)
btn_subtraction = tk.Button(root, text='-', padx=9,
                            pady=0, width=8, command=lambda: btn_click('-'))
btn_subtraction.grid(row=5, column=4)

btn_0 = tk.Button(root, text='0', padx=9, pady=0,
                  width=8, command=lambda: btn_click('0'))
btn_0.grid(row=6, column=0)
btn_00 = tk.Button(root, text='00', padx=9, pady=0,
                   width=8, command=lambda: btn_click('00'))
btn_00.grid(row=6, column=1)
btn_period = tk.Button(root, text='.', padx=9, pady=0,
                       width=8, command=lambda: btn_click('.'))
btn_period.grid(row=6, column=2)
btn_equal = tk.Button(root, text='=', padx=9, pady=0, width=8, command=equals)
btn_equal.grid(row=6, column=3, columnspan=2, sticky='ew')

populate_tape()

root.mainloop()
