# https://drive.google.com/file/d/1s2TJH56ulUi4TawlZt_mQp7UibNi35eh/view?usp=sharing
#
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# Решение с помощью рекурсии

def reverse(a, b = 0):
    if a // 10 == 0:
        return b * 10 + a
    else:
        return reverse(a // 10, (10 * b) + (a % 10))

num = int(input('Введи число: '))
z = reverse(num)
print(z)

# Решение через цикл
#n = int(input('Введи число: '))
#m = 0
#while n > 0:
#    m = m * 10 + n % 10
#    n = n // 10
#print(m)
