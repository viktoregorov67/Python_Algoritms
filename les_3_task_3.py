# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

array[min_ind], array[max_ind] = array[max_ind], array[min_ind]

print(array)
