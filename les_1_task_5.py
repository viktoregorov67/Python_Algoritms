# https://drive.google.com/file/d/1ZWDqhbm7fVTG-TvGHkXzhr8WkxH-Tllu/view?usp=sharing
#
# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
lenght = abs(a - b) - 1
print(f'Позиции: {a} и {b}')

print(f'Между буквами расположено {lenght} букв.')

