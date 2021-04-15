import decimal
import settings
from tkinter import messagebox


def generate_error_message():
    messagebox.showerror('Message from Application', settings.error)
    return


def check_bad_operators(input):
    operators = ['+', 'x', '/']
    for i in range(len(input)):
        if i > 0:
            if input[i] in operators and input[i-1] == input[i]:
                settings.error = "Bad Form: " + input[i-1] + input[i] + " together."
                return True
            if input[i] in operators and input[i-1] in operators:
                settings.error = "Bad Form: " + input[i-1] + input[i] + " together."
                return True
            if input[i-1] == '-' and input[i] in operators:
                settings.error = "Bad Form: " + input[i-1] + input[i] + " together."
                return True
            if i == len(input)-1:
                if input[i] == '-' or input[i] in operators:
                    settings.error = "Bad Form: Operator " + input[i] + " at the end"
                    return True
    return False


def number_check(n):
    temp = ''
    for i in range(len(n)):
        if n[i].isdigit():
            temp += n[i]
        elif n[i] == '.':
            temp += n[i]
        elif n[i] == '-' and i == 0:
            temp += n[i]
        else:
            return False
    return True


def check_if_float(n):
    number1 = n
    if n[0] == '-':
        number1 = number1.lstrip('-')
        if number1.isdigit():
            return False
        else:
            return True
    else:
        if number1.isdigit():
            return False
        else:
            return True


def operation(number1, number2, operator):
    number1 = str(number1)
    number2 = str(number2)

    if check_if_float(number1):
        number1 = float(number1)
    else:
        number1 = int(number1)

    if check_if_float(number2):
        number2 = float(number2)
    else:
        number2 = int(number2)

    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == 'x':
        return number1 * number2
    if operator == '/':
        if number2 == 0:
            generate_error_message("Division by Zero: Undefined")
        else:
            return number1 / number2


def process(op_list, operator, function):
    index = op_list.index(operator)
    size = len(op_list)
    if index + 1 == size - 1:
        op_list.append(function(decimal.Decimal(
            op_list[index-1]), decimal.Decimal(op_list[index+1]), operator))
    else:
        op_list.insert(index+2, function(decimal.Decimal(
            op_list[index-1]), decimal.Decimal(op_list[index+1]), operator))
    op_list.pop(index-1)
    op_list.pop(index-1)
    op_list.pop(index-1)
    return op_list


def run_process(op_list, operator):
    if operator == 'x' or operator == '/' or operator == '+' or operator == '-' and operator in op_list:
        return process(op_list, operator, operation)


def apply_pemdas(list1):
    while 'x' or '/' in list1:
        for i in range(len(list1)):
            if i + 1 > len(list1):
                break
            if list1[i] == 'x' or list1[i] == '/':
                list1 = run_process(list1, list1[i])
        if 'x' not in list1 and '/' not in list1:
            break
    while '+' or '-' in list1:
        for j in range(len(list1)):
            if j + 1 > len(list1):
                break
            if list1[j] == '+' or list1[j] == '-':
                list1 = run_process(list1, list1[j])
        if '+' not in list1 and '-' not in list1:
            break
    return list1


def filter_numbers(op_string):
    temp = ''
    op_list = list(temp)
    operators = ['+', 'x', '/']
    t1 = ''
    for i in range(len(op_string)):
        if op_string[i].find('+') == -1 and op_string[i].find('-') == -1 and op_string[i].find('x') == -1 and op_string[i].find('/') == -1:
            t1 = t1 + op_string[i]
            if i == len(op_string)-1:
                op_list.append(t1)
                t1 = ''
        else:
            if op_string[i] == '-' and i == 0:
                t1 += op_string[i]
            elif op_string[i] == '-' and op_string[i-1] == '-':
                t1 += op_string[i]
            elif op_string[i-1] in operators and op_string[i] == '-':
                t1 += op_string[i]
            else:
                op_list.append(t1)
                op_list.append(op_string[i])
                t1 = ''
        if '' in op_list:
            op_list.remove('')

    return apply_pemdas(op_list)
