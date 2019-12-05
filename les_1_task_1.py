# https://drive.google.com/file/d/1ZWDqhbm7fVTG-TvGHkXzhr8WkxH-Tllu/view?usp=sharing
#
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите трехзначное число: '))

c = number % 10

number = number // 10
b = number % 10

a = number // 10

summ = a + b + c
mult = a * b * c

print(f'Сумма цифр числа = {summ}')
print(f'Произведение цифр числа = {mult}')

