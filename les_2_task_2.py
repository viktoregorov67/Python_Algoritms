# https://drive.google.com/file/d/1s2TJH56ulUi4TawlZt_mQp7UibNi35eh/view?usp=sharing
#
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введи число: '))

even = 0
odd = 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print(f'В числе нечетных цифр - {odd}, четных - {even}.')