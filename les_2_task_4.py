# https://drive.google.com/file/d/1s2TJH56ulUi4TawlZt_mQp7UibNi35eh/view?usp=sharing
#
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введи количество элементов ряда: '))
# Определим значение первого элемента ряда и суммы
a = 1
sum = 0

for i in range(n):
    sum += a
    a /= -2

print(sum)

