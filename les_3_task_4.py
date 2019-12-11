# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# Определяем начальные значения
num_arr = array[0]
max_itm = 1

# Сравниваем элементы массива до и считаем сколько раз встречается каждый элемент
for i in range(SIZE - 1):
    itm = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            itm += 1
    if itm > max_itm:
        max_itm = itm
        num_arr = array[i]

if max_itm > 1:
    print(f'Элемент {num_arr} встречается {max_itm} раз.')
else:
    print('В массиве все элементы уникальны.')
