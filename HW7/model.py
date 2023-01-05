
first_number = 0
second_number = 0
operation = ''
result = 0
mode = 0
expression = ''
result_expression = 0

def set_mode(select):
    global mode
    mode = select

def get_mode():
    global mode
    return mode

def get_first():
    global first_number
    return first_number

def get_second():
    global second_number
    return second_number

def get_operation():
    global operation
    return operation

def get_result():
    global result
    return result

def get_expression():
    global expression
    return expression

def get_result_expression():
    global result_expression
    return result_expression

def set_first(value):
    global first_number
    first_number = value

def set_second(value):
    global second_number
    second_number = value

def set_operation(oper):
    global operation
    operation = oper

def set_expression(string):
    global expression
    expression = string

def additional():
    global first_number, second_number, result
    result = first_number + second_number

def difference():
    global first_number, second_number, result
    result = first_number - second_number

def multiplication():
    global first_number, second_number, result
    result = first_number * second_number

def division():
    global first_number, second_number, result
    result = first_number / second_number
    if result == int(result):
        result = int(result)

def parsing_expression():
    global expression, result_expression

    list_expression = expression.split()

    for i in range(len(list_expression)):
        if list_expression[i].isdigit():
            list_expression[i] = int(list_expression[i])

    result_num = 0

    while len(list_expression) != 1:
        i = 0
        while ('*' in list_expression or '/' in list_expression) and i < len(list_expression):
            if list_expression[i] == '*':
                result_num = list_expression[i - 1] * list_expression[i + 1]
                list_expression.pop(i)
                list_expression.pop(i)
                list_expression[i - 1] = result_num
            elif list_expression[i] == '/':
                result_num = list_expression[i - 1] / list_expression[i + 1]
                list_expression.pop(i)
                list_expression.pop(i)
                list_expression[i - 1] = result_num
            else:
                i += 1

        while ('+' in list_expression or '-' in list_expression) and i < len(list_expression):
            if list_expression[i] == '+':
                result_num = list_expression[i - 1] + list_expression[i + 1]
                list_expression.pop(i)
                list_expression.pop(i)
                list_expression[i - 1] = result_num
            elif list_expression[i] == '-':
                result_num = list_expression[i - 1] - list_expression[i + 1]
                list_expression.pop(i)
                list_expression.pop(i)
                list_expression[i - 1] = result_num
            else:
                i += 1
    result_expression = list_expression[0]


