# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

def sum_HEX(num1_, num2_):

    table_HEX_DEC = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    table_DEC_HEX = {val:key for key, val in table_HEX_DEC.items()}

    num1 = deque(num1_)
    num2 = deque(num2_)

    if len(num2) > len(num1):
        max_len = len(num2)
        num1.extendleft('0' * (max_len - len(num1)))
    else:
        max_len = len(num1)
        num2.extendleft('0' * (max_len - len(num2)))

    sum_ = deque()
    mem = 0

    for i in range(1, max_len + 1):
        ans_ = table_HEX_DEC[num1.pop()] + table_HEX_DEC[num2.pop()] + mem

        mem = 1 if ans_ >= 16 else 0
        ans_ = ans_ + (-16 * mem)

        sum_.extendleft(table_DEC_HEX[ans_])

    if mem > 0:
        sum_.appendleft(mem)

    return ''.join(sum_)

def mul_HEX(num1_, num2_):
    table_HEX_10 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    table_DEC_HEX = {val:key for key, val in table_HEX_10.items()}

    num1 = deque(num1_)
    num2 = deque(num2_)

    if len(num2) > len(num1):
        max_len = len(num2)
        min_len = len(num1)
        op1 = num2
        op2 = num1
    else:
        max_len = len(num1)
        min_len = len(num2)
        op1 = num1
        op2 = num2
    res = ''
    for j in range(1, min_len + 1):
        mul_ = deque()
        mem = 0
        for i in range(1, max_len + 1):
            ans_ = table_HEX_DEC[op1[-i]] * table_HEX_DEC[op2[-j]] + mem
            mem = ans_ // 16 if ans_ >= 16 else 0
            ans_ = table_DEC_HEX[ans_ - (16 * mem)]
            mul_.appendleft(ans_)

        if mem > 0:
            mul_.appendleft(str(mem))
        if j > 1:
            mul_.append('0')
        res = sum_HEX(res, ''.join(mul_))
    return res

while True:
    sign = input('Выберите операцию введя соответствующий знак (+, *), 0 завершает работу: ')
    if sign == '0':
        break
    if sign in {'+', '*'}:
        if sign == '+':
            print(sum_HEX(
                input('Введите первое слагаемое в HEX: ').upper(),
                input('Введите второе слагаемое в HEX: ').upper()
            ))
        if sign == '*':
            print(mul_HEX(
                input('Введите первый множитель в HEX: ').upper(),
                input('Введите второй множитель в HEX: ').upper()
            ))

