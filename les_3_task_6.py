# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ind = 0
max_ind = 0
# Находим индекс максимального и минимального элемента
for i in range(SIZE):
    if array[i] < array[min_ind]:
        min_ind = i
    elif array[i] > array[max_ind]:
        max_ind = i

print(f'Минимальный эемент массива - {array[min_ind]}, максимальный - {array[max_ind]}')

#Если минимальный элемент массива расположен после максимального
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

# Находим сумму элементов
item_sum = 0
for i in range(min_ind + 1, max_ind):
    item_sum += array[i]

print(f'Сумма элементов между min и max элементами равна{item_sum}')




