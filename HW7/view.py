# выбор режима калькулятора
def mode_selection() -> int:
    while True:
        try:
            mode = int(input('Какой режим вы выберите?(1 или 2): '))
            if mode == 1 or mode == 2:
                return mode
            else:
                print('Некорректный ввод. Попробуйте еще раз.')
        except:
            print('Некорректный ввод. Попробуйте еще раз.')

def input_number() -> int:
    while True:
        try:
            number = int(input('Введите число: '))
            return number
        except:
            print('Ошибка')

def input_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию.')

def input_expression() -> str:
    while True:
        counter = 0
        expression = input('Введите выражение: ')
        if len(expression) < 3:
            counter += 1
        if expression[0] in ['+', '-', '*', '/']:
            counter += 1
        for char in expression:
            if char in '1234567890' or char in ['+', '-', '*', '/', ' ', '(', ')']:
                pass
            else:
                counter += 1
        if counter == 0:
            return expression
        else:
            print('Ввели некорректные данные. Попробуйте еще раз')
            print()

def print_to_console(value_text):
    print(value_text)

def log_off():
    print('До свидания!')

def print_division_by_zero():
    print('На ноль делить нельзя!')

def greetings():
    print('Программа калькулятор, работает как "шаг за шагом"(1), или с целым выражением(2).')
    print()

def rules_1():
    print()
    print('Режим "шаг за шагом".\nСначала вы вводите первое число, после операцию и второе число.\n'
          'После вы работаете с полученным результатом, вводя операцию и второе число.\n'
          'Знак "=" выведет вас из программы.')
    print()

def rules_2():
    print()
    print('Режим строковый.\n'
          'Пример выражения для ввода: 1 + 2 * 4 - 1')
    print()
