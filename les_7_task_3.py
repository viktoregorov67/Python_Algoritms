# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
# равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = 3
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * m + 1)]
print(array)


def find_median(array):
    if len(array) > 1:
        for i in array:
            left_i = 0
            right_i = 0
            for j in array:
                if j < i:
                    left_i += 1
                elif j > i:
                    right_i += 1
                else:
                    left_i += 1
                    right_i += 1
            if left_i == right_i:
                return i
    else:
        return array[0]


print(find_median(array))


