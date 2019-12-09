# https://drive.google.com/file/d/1s2TJH56ulUi4TawlZt_mQp7UibNi35eh/view?usp=sharing
#
# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


def r_sum(n):
    if n <= 1:
        return n
    else:
        return n + r_sum(n - 1)

n = int(input('Введи натуральное число: '))
a = r_sum(n)
b = n * (n + 1) // 2
if a == b:
    print(f'Равенство 1+2+...+n = n(n+1)/2, где n = {n} верно. {a} = {b}')
else:
    print(f'Равенство 1+2+...+n = n(n+1)/2, где n = {n} неверно. {a} != {b}')



