# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

# Вариант 1. Сначала решил с помощью словаря (можно считать коллекцией).
# companies = {}
# n = int(input('Введите количество предприятий: '))
# s = 0
# for i in range(n):
#     money_year = 0
#     name = input(f'{i + 1}-е предприятие - ')
#     for j in range(4):
#         money = int(input(f'Прибыль за {j + 1} квартал: '))
#         money_year += money
#     avrg_money = money_year / 4
#     companies[name] = avrg_money
#     s += avrg_money
#
# avrg = s / n
# print(f'Средняя прибыль всех предприятий за год - {avrg}')
# print(f'Предприятия с прибылью выше среднего: ')
# for i in companies:
#     if companies[i] > avrg:
#         print(i)
#
# print(f'Предприятия с прибылью ниже среднего: ')
# for i in companies:
#     if companies[i] < avrg:
#         print(i)

# Вариант 2. Затем решил использовать именно коллекции.
from collections import Counter

companies = {}
n = int(input('Введите количество предприятий: '))
s = Counter()

for i in range(n):
    name = input(f'{i + 1}-е предприятие - ')
    money_year = 0
    for j in range(4):
        money = int(input(f'Прибыль за {j + 1} квартал: '))
        money_year += money
    avrg_money = money_year / 4
    companies[name] = Counter(
        {
            'money_year': money_year,
            'avrg_money': avrg_money
        }
    )
    s += companies[name]

print(companies)
avrg = s['money_year'] / n
print(f'Средняя прибыль всех предприятий за год - {avrg}')
# Вывод на печать можно было сделать немного иначе
high_avrg = []
low_avrg = []
for i in companies:
     if companies[i]['money_year'] > avrg:
         high_avrg.append(i)
     else:
         low_avrg.append(i)

print(f'Предприятия с прибылью выше среднего: {high_avrg}')
print(f'Предприятия с прибылью выше среднего: {low_avrg}')
