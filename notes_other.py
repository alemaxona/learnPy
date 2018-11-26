__author__ = 'alemaxona'


# Условие в одну строку:
def user_func(a=None):
    return a + 3 if a != None else 'It\'s none'


print(user_func(2))
print(user_func())
# 5
# It's none

# Работа с файлами
# Создание, чтение, запись и добавление в\из файл\а
filename = 'file_create_with_python.txt'
open(filename, 'a')  # Создание фала в текущей дирректории
open('file.txt', 'r')  # r - read - Чтение из файла
open('file.txt', 'w')  # w - write  - Запись из файла
open('file.txt', 'a')  # a - append - Добавление в конец строки файла
# Обязательно нужно закрывать файл!
f = open('file.txt')
f.close()


# Эквивалентные операции.
with open('file.txt', 'w') as f:  # with - Закрывает файл и удаляет мусор даже, если будет ошибка.
    f.write('Hello world!')

f = open('file.txt', 'r')
# Если тут будет ошибка, файл не закроется!
print(f.read())
f.close()


# Создание каталога (в windows)
from os import *
source = r'C:\Project\dir_create_with_python'  # r - отключает механизм экранирования
makedirs(source)


# Задачка Егора
s = 'TBTXDB01.interrao.ru\nDB_USER=2\nDB_PASS=1\n#DB_NAME=tbtxdb01_test_20171116\n' \
    '#DB_NAME=app04_db01_20180122\n#DB_NAME=app04_db01_201800205\n' \
    '#DB_NAME=app04_db01_20180329\n#DB_NAME=app04_db01_20180619\n' \
    'DB_NAME=app04_db01_20180927\nDEBUG=true\nDISPOSER_SITE_FOLDER=interrao\nFILE_CACHE=false\n"]'
output = s.split('\n')


def pars_str(string):
    for i in string:
        if i[0] == 'D' and \
                i[1] == 'B' and \
                i[2] == '_' and \
                i[3] == 'N':
            out = i.split('=')
            return out[1]


print(pars_str(output))


# Копирование (.copy()) очень аккуратно! (https://pythonworld.ru/moduli/modul-copy.html)
a = {}
b = [[0, 0], [1, 1], [2, 2]]
a[0] = b.copy()
a[1] = b.copy()
print(a)
# {0: [[0, 0], [1, 1], [2, 2]], 1: [[0, 0], [1, 1], [2, 2]]}

a[0][0][1] = '*'  # Поменядось сразу в двух списках!
print(a)
# {0: [[0, '*'], [1, 1], [2, 2]], 1: [[0, '*'], [1, 1], [2, 2]]}

print(id(b[0][1]))  # Так как это просто ссылки на один и тот же элемент в памяти!
print(id(a[0][0][1]))

# Нужно использовать:
from copy import deepcopy

a = {}
b = [[0, 0], [1, 1], [2, 2]]

a[0] = deepcopy(b)
a[1] = deepcopy(b)
print(a)
# {0: [[0, 0], [1, 1], [2, 2]], 1: [[0, 0], [1, 1], [2, 2]]}

a[0][0][1] = '*'
print(a)
# {0: [[0, '*'], [1, 1], [2, 2]], 1: [[0, 0], [1, 1], [2, 2]]}

print(id(b[0][1]))
# 1774336240

int(id(a[0][0][1]))
# 2534080


# Оператор continue - возвращает в начало цикла!
while True:
    a = input('X: ')
    b = input('Y: ')
    if int(a) == 0 and int(b) == 0:
        break  # Завершает цикл, не доходя до конца!
    if int(a) == 0 or int(b) == 0:
        continue  # Переходит в начало цикла, не доходя до конца!
    c = a + b
    print(c)


'''
Очень важно!
При создании двумерного списка(наподобие матрицы) необходимо пользоваться генераторами!
Без генератора получается следущее:
'''

n = 3
a = [[0] * n] * n
print(a)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 5
print(a)
# [[5, 0, 0], [5, 0, 0], [5, 0, 0]]  # Так как переменная просто использует (в данном случае) 3 ссылки на список n!


# С генератором:
a = [[0] * n for i in range(n)]
a[0][0] = 5
# [[5, 0, 0], [0, 0, 0], [0, 0, 0]]
# Или
a = [[0 for j in range(n)] for i in range(n)]
a[0][0] = 5
# [[5, 0, 0], [0, 0, 0], [0, 0, 0]]

#
a = ['s', 'b', 'g']

print(range(len(a)))
# range(0, 3)

for i in range(len(a)):
    print(a[i])
# s
# b
# g


# Встроенные объекты. (list, int, dict, len...)

import builtins  # Можно не импортировать!
print(dir(__builtins__))


# Короткая запись - Списковые выражения:
s = [w for w in range(1, 14)]
print(s)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

s = [w for w in range(1, 14) if w % 2 == 0]
print(s)
# [2, 4, 6, 8, 10, 12]


import os
print(os)
# <module 'os' from '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py'>


# Сравнение
1 == 1  # По сути сравнение ячеек памяти.

a = 257
b = 257  # Так как > 256 (С кешем связано...)
a is b
# False
id(a), id(b)
# (31833360, 31833120)

a = 256
b = 256
a is b
# True
id(a), id(b)  # Посмотреть ячейку памяти
# (266881264, 266881264)

1 == True
# True
1 is True
# False


# Help
help(object)


# Функция isinstance() специально создана для проверки принадлежности данных определенному классу (типу данных).
isinstance(a, int)
# True
isinstance(b, list)
# True
isinstance(b, tuple)
# False
c = (4, 5, 6)
isinstance(c, tuple)
# True

#  Если словарь пустой то возвращается False!
bool({})  # По сути идет сравнение длины, если длина = 0, то возвращается False!
# False
bool({'Max': 5})
# True

# Сравнение едит по ключам!
2 in {'1': 2}
# False
'1' in {'1': 2}
# True


# Короткая запись условия
value = 2

if value > 0:
    print(str(value))
else:
    print('')

# ==

print(str(value) if value > 0 else print(''))


# index letter
chose = 'max'
c = 'm'
index = 0
c == chose[index]
# True
a = chose[index]
print(a)
# m


#
s, k = (1, 2)  # Но не s,k,m = (1,2)
print(s, k)
# 1 2

first, *second = (1, 2, 3, 4, 5)
print(first, second)
# 1 [2, 3, 4, 5]

*f, s = 'Moscow'
print(f)
# ['M', 'o', 's', 'c', 'o']


#
print('Word', end='!')
# Word!>>>

print('Word', end='\n')
# Word
# >>>
print('Max', end='!')  # Не переходит на новую строку
print('Max', end='\n')


# RANDOM
from random import randint
value = randint(0, 20)
print(value)
# 12

import random
items = ['one', 'two', 'three', 'four', 'five']
random.choice(items)
# 'four'

#
tuple1 = (1, 2, 'string', 'one more', )
new_tuple = tuple()
for item in tuple1:
    # if not isinstance(item, (str, unicode)):  # or `basestring`
    if not isinstance(item, str):  # Если этот елемент не строка
        new_tuple += (item, )  # new_tuple = new_tuple + (item, )
print(new_tuple)
# (1, 2)

#
list1 = [1, 2]
list2 = [7, 8]
list1.append(list2)  # Мутация, append - добавление в список 1 елемент
print(list1)
# [1, 2, [7, 8]]

list1.extend(list2)  # Мутация, extend - добавление нескольких елементов
print(list1)
# [1, 2, 7, 8]

list1.insert(1, 'str')  # Не стоит использовать! 1 здесь позиция в list
# list1.pop(1)  # Delete element for index
# list1.remove('2')  # Delete element for value
# del list1[0]  # Delete element for index !Некрасивая версия pop!


list(range(1, 10, 1))  # Генератор. 3 параметр - шаг
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Все ключи в словаре уникальные!
# Неизменяемый тип данных не может быть ключем!
s = {'a': 'a', 1: 'str', None: 3}
s.update({2: 'q'})  # Мутация в словаре. Добавить пару ключ - значение
s[2] = None
# s[ma] # Выдаст ошибку, так как ключа такого нет
# s.get(ma) # Ошибку не выдаст, но и результат тоже.
# s.keys() # Получить ключи словаря
# s.values() # Получить елементы словаря
for k in s:
    print(k, s[k])
# s s
# 1 str
# None 3

for k, v in s.items():  # ==
    print(k, v)
# s s
# 1 str
# None 3

# s.pop('s')  # Удаляет и ключ и значение
