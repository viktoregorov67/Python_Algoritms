# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile

# Алгоритм 1. Решето Эратосфена

def sieve(n):
    arr_sieve = [i for i in range(n**2)]
    arr_sieve[1] = 0
    for i in range(2, n**2):
        if arr_sieve[i] == 0: continue
        for j in range(2*i, n**2, i):
            arr_sieve[j] = 0

    res = [i for i in arr_sieve if i != 0]
    return res[n]


# s = """
# def sieve(n):
#     arr_sieve = [i for i in range(n**2)]
#     arr_sieve[1] = 0
#     for i in range(2, n**2):
#         if arr_sieve[i] == 0: continue
#         for j in range(2*i, n**2, i):
#             arr_sieve[j] = 0
#
#     res = [i for i in arr_sieve if i != 0]
#     return res[n]
#
# sieve(1000)
# """

# Алгоритм 2. Метод простой поочередной проверки каждого числа на простоту
def prime(n):
    a = 1
    array = [2]
    while len(array) < n:
        a += 2
        for i in array:
            if a % i == 0:
                break
        else:
            array.append(a)
    return array[-1]

# s = """
# def prime(n):
#     a = 1
#     array = [2]
#     while len(array) < n:
#         a += 2
#         for i in array:
#             if a % i == 0:
#                 break
#         else:
#             array.append(a)
#     return array[-1]
#
# prime(1000)
# """


# Блок проверок
# print(timeit.timeit(s, number=100))

# timeit для sieve
# 0.014700099999999994 sieve(10)
# 0.0598689 sieve(20)
# 0.2542755 sieve(40)
# 1.7297927000000002 sieve(100)
# 6.952881400000001 sieve(200)
# 205.4928369 sieve(1000)

# timeit для prime
# 0.0034288000000000096 prime(10)
# 0.010049200000000008 prime(20)
# 0.03278199999999999 prime(40)
# 0.204111 prime(100)
# 0.6932891 prime(200)
# 17.6649078 prime(1000)

cProfile.run('prime(1000)')
# sieve(100)
# 1    0.000    0.000    0.025    0.025 <string>:1(<module>)
# 1    0.022    0.022    0.025    0.025 les_4_task_2.py:11(sieve)
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:12(<listcomp>)
# 1    0.002    0.002    0.002    0.002 les_4_task_2.py:19(<listcomp>)
# 1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}

# sieve(1000)
# 1    0.027    0.027    2.380    2.380 <string>:1(<module>)
# 1    1.941    1.941    2.353    2.353 les_4_task_2.py:11(sieve)
# 1    0.229    0.229    0.229    0.229 les_4_task_2.py:12(<listcomp>)
# 1    0.183    0.183    0.183    0.183 les_4_task_2.py:19(<listcomp>)
# 1    0.000    0.000    2.380    2.380 {built-in method builtins.exec}

# prime(100)
# 1    0.000    0.000    0.002    0.002 <string>:1(<module>)
# 1    0.002    0.002    0.002    0.002 les_4_task_2.py:39(prime)
# 1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
# 271    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# prime(100)
# 1    0.000    0.000    0.247    0.247 <string>:1(<module>)
# 1    0.242    0.242    0.247    0.247 les_4_task_2.py:39(prime)
# 1    0.000    0.000    0.247    0.247 {built-in method builtins.exec}
# 3960    0.004    0.000    0.004    0.000 {built-in method builtins.len}
# 999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

# Предположительно, алгоритм сложности O(n**2). Для обоих способов. Но при выполнении перебора у нас возникают рекурсии.
# Но меня терзают смутные сомнения что что-то пошло не так или я где-то ошибся.
# Логически предполагаю что алгоритм решета Эратосфена должен работать быстрее, особенно на больших числах.


