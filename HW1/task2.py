# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'Для значения {x}, {y}, {z} истинность выражения является --> '
                  f'{not(bool(x) or bool(y) or bool(z)) == (not(bool(x)) and not(bool(y)) and not(bool(z)))}')