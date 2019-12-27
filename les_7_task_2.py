# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random() * MAX_ITEM for _ in range(SIZE)]
print(array)

def merge_sort(array):
    if len(array) > 1:
        split = len(array) // 2
        left_half = array[:split]
        right_half = array[split:]

        merge_sort(left_half)
        merge_sort(right_half)

        n = 0
        n1 = 0
        n2 = 0
        while n1 < len(left_half) and n2 < len(right_half):
            if left_half[n1] < right_half[n2]:
                array[n] = left_half[n1]
                n1 += 1
            else:
                array[n] = right_half[n2]
                n2 += 1
            n += 1

        while n1 < len(left_half):
            array[n] = left_half[n1]
            n1 += 1
            n += 1

        while n2 < len(right_half):
            array[n] = right_half[n2]
            n2 += 1
            n += 1

    return array


print(merge_sort(array))