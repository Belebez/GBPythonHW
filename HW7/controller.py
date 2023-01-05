import view
import model

def input_mode():
    number = view.mode_selection()
    model.set_mode(number)

def input_first():
    number = view.input_number()
    model.set_first(number)

def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break

def input_operation():
    oper = view.input_operation()
    model.set_operation(oper)

def solution():
    oper = model.get_operation()
    match oper:
        case '+':
            model.additional()
        case '-':
            model.difference()
        case '*':
            model.multiplication()
        case '/':
            model.division()

    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first((model.get_result()))

def input_expression():
    string = view.input_expression()
    model.set_expression(string)

def solution_expression():
    model.parsing_expression()
    result_string = f'Решение вашего выражения: {model.get_expression()} = {model.get_result_expression()}'
    view.print_to_console(result_string)

def start():
    view.greetings()
    input_mode()
    if model.get_mode() == 1:
        view.rules_1()
        input_first()
        while True:
            input_operation()
            if model.get_operation() == '=':
                view.log_off()
                break
            input_second()
            solution()
    elif model.get_mode() == 2:
        while True:
            view.rules_2()
            input_expression()
            solution_expression()
            replace = input('Хотите посчитать другое выражение?(y/n) --> ')
            if replace.lower() == 'n':
                break
