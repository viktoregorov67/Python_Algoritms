# https://drive.google.com/file/d/1ZWDqhbm7fVTG-TvGHkXzhr8WkxH-Tllu/view?usp=sharing
#
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Введите номер буквы в алфавите: '))
n = ord('a') + n - 1
n = chr(n)
print(f'Это буква {n}.')
