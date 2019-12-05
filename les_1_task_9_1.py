# https://drive.google.com/file/d/1ZWDqhbm7fVTG-TvGHkXzhr8WkxH-Tllu/view?usp=sharing
#
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Первый вариант решения (

print('Введите 3 числа')
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
if a > b:
    if b > c:
        print(f'Среднее число равно {b}')
    elif a > c:
        print(f'Среднее число равно {c}')
    else:
        print(f'Среднее число равно {a}')
else:
    if b < c:
        print(f'Среднее число равно {b}')
    elif a < c:
        print(f'Среднее число равно {c}')
    else:
        print(f'Среднее число равно {a}')

