# Домашняя работа
# n = int(input('Enter n: '))
# number = 0
# str = f'{n} -> '
#
# while 2 ** number < n:
#     str += f'{2 ** number} '
#     number += 1
#
# print(str)

# import random
#
# n = int(input("Enter n: "))
# str = f''
# orel = 0
# reshka = 0
# for i in range(n):
#     moneta = round(random.uniform(0, 1))
#     str += f' {moneta}'
#     if moneta == 0:
#         orel += 1
#     else:
#         reshka += 1
# print(str)
# print(f'Надо перевернуть решку - {reshka} шт' if orel > reshka else f'Надо перевернуть орлов - {orel}')

import random

a = round(random.uniform(0, 1000))
b = int(round(random.uniform(0, 1000)))
# для проверки
# print(a, b)
print('Петя загадал число...')
summa = a + b
print(f'Подсказка 1: {summa} ')
multiplication = a * b
print(f'Подсказка 2: {multiplication} ')
for i in range(summa):
    if i * (summa - i) == multiplication:
        print(i, summa - i)
        break
