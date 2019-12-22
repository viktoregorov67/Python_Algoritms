# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

# Windows 10 64-bit, 8 Gb RAM  Python 3.8.0 32-bit

# Для примера взял задачу из 3 урока:
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import sys
import random

def show_size(x, level=0):
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    size_value.append(sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


# Вариант 1
size_value = []

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ind = 0
max_ind = 0
for i in range(len(array)):
    if array[i] < array[min_ind]:
        min_ind = i
    elif array[i] > array[max_ind]:
        max_ind = i

array[min_ind], array[max_ind] = array[max_ind], array[min_ind]
print(array)

show_size(array)
show_size(SIZE)
show_size(MIN_ITEM)
show_size(MAX_ITEM)
show_size(min_ind)
show_size(max_ind)
show_size(i)
show_size(array[min_ind])
show_size(array[max_ind])
print(f'Под переменные выделено -  {sum(size_value)} байт.')
# Результаты работы:
#   type=<class 'list'>, size=92, obj=[33, -91, 32, -38, 88, 86, -56, -32, 97, 21]
# 	 type=<class 'int'>, size=14, obj=33
# 	 type=<class 'int'>, size=14, obj=-91
# 	 type=<class 'int'>, size=14, obj=32
# 	 type=<class 'int'>, size=14, obj=-38
# 	 type=<class 'int'>, size=14, obj=88
# 	 type=<class 'int'>, size=14, obj=86
# 	 type=<class 'int'>, size=14, obj=-56
# 	 type=<class 'int'>, size=14, obj=-32
# 	 type=<class 'int'>, size=14, obj=97
# 	 type=<class 'int'>, size=14, obj=21
#  type=<class 'int'>, size=14, obj=10
#  type=<class 'int'>, size=14, obj=-100
#  type=<class 'int'>, size=14, obj=100
#  type=<class 'int'>, size=14, obj=8
#  type=<class 'int'>, size=14, obj=1
#  type=<class 'int'>, size=14, obj=9
#  type=<class 'int'>, size=14, obj=97
#  type=<class 'int'>, size=14, obj=-91
# Под переменные выделено -  344 байт.


print('=' * 30)

# Вариант 2
size_value = []

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

show_size(array)
show_size(SIZE)
show_size(MIN_ITEM)
show_size(MAX_ITEM)
show_size(min_num)
show_size(max_num)
show_size(min(array))
show_size(max(array))
show_size(idx_min)
show_size(idx_max)
show_size(array[idx_min])
show_size(array[idx_max])
print(f'Под переменные выделено -  {sum(size_value)} байт.')

# Результаты работы:
# type=<class 'list'>, size=92, obj=[-1, 58, 87, 27, 59, -28, -13, 41, -83, -99]
# 	 type=<class 'int'>, size=14, obj=-1
# 	 type=<class 'int'>, size=14, obj=58
# 	 type=<class 'int'>, size=14, obj=87
# 	 type=<class 'int'>, size=14, obj=27
# 	 type=<class 'int'>, size=14, obj=59
# 	 type=<class 'int'>, size=14, obj=-28
# 	 type=<class 'int'>, size=14, obj=-13
# 	 type=<class 'int'>, size=14, obj=41
# 	 type=<class 'int'>, size=14, obj=-83
# 	 type=<class 'int'>, size=14, obj=-99
#  type=<class 'int'>, size=14, obj=10
#  type=<class 'int'>, size=14, obj=-100
#  type=<class 'int'>, size=14, obj=100
#  type=<class 'int'>, size=14, obj=-99
#  type=<class 'int'>, size=14, obj=87
#  type=<class 'int'>, size=14, obj=-99
#  type=<class 'int'>, size=14, obj=87
#  type=<class 'int'>, size=14, obj=2
#  type=<class 'int'>, size=14, obj=9
#  type=<class 'int'>, size=14, obj=87
#  type=<class 'int'>, size=14, obj=-99
# Под переменные выделено -  386 байт.

# Можно сделать выводы что в первом варианте места под переменные выделяется меньше.
