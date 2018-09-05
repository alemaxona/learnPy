# Add __doc__ to function!
def print_doc():
    '''Notes for learning.

    This learning Python 3 notes.
    Here more error.'''
print(print_doc.__doc__)


# index letter
chose = 'max'
c = 'm'
index = 0
c == chose[index]
#True
a = chose[index]
print(a)
#m

#RANDOM
from random import randint
value = randint(0, 20)
print(value)
#12

import random
items = ['one', 'two', 'three', 'four', 'five']
random.choice(items)
#'four'

#
tuple1 = (1, 2, 'string', 'one more', )
new_tuple = tuple()
for item in tuple1:
    # if not isinstance(item, (str, unicode)):  # or `basestring`
    if not isinstance(item, str): # Если этот елемент не строка
        new_tuple += (item, ) # new_tuple = new_tuple + (item, )
print(new_tuple)
#(1, 2)

#
list1 = [1, 2 ]
list2 = [7, 8 ]
list1.append(list2) # Мутация, append - добавление в список 1 елемент
print(list1)
#[1, 2, [7, 8]]

list1.extend(list2) # Мутация, extend - добавление нескольких елементов
print(list1)
#[1, 2, 7, 8]

list1.insert(1, 'str') # Не стоит использовать! 1 здесь позиция в list
#list1.pop(1) # Delete element for index
#list1.remove('2') # Delete element for value
#del list1[0] # Delete element for index !Некрасивая версия pop!


for row in multi:
    for element in row:

list(range(1, 10, 1)) # Генератор. 3 параметр - шаг
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

# Все ключи в словаре уникальные!
# Неизменяемый тип данных не может быть ключем!
s = {'a' : 'a', 1 : 'str', None : 3}
s.update({2: 'q'}) #Мутация в словаре. Добавить пару ключ - значение
s[2] = None
#s[ma] # Выдаст ошибку, так как ключа такого нет
#s.get(ma) # Ошибку не выдаст, но и результат тоже.
#s.keys() # Получить ключи словаря
#s.values() # Получить елементы словаря
for k in s:
    print(k, s[k])
#s s
#1 str
#None 3

for k, v in s.items():
    print(k, v)
#s s
#1 str
#None 3

#s.pop('s') # Удаляет и ключ и значение

#
try:
    print(1 / 0)
except Exception:  # it is almost the same as just `except:`
    print('0!!')
#
#try:
#    1 / 0
#except ValueError: # Не сработает так как ошибка ZeroDivisionError а не ValueError!
#    print('0!!')

try:
    1 / 0
except ZeroDivisionError: # Сработает так как ошибка ZeroDivisionError!
    print('0!!')
#
try:
    1 / int(input('x: '))
except ZeroDivisionError:
    print('/0')
except TypeError:
    print('WrongValue')

#
try:
    print(1 / 0)
except ZeroDivisionError as e: # В переменную!
    print('Exception! Stop it!')
    print(e)
#
raise IndexError('Hi!') # Выкинуть ошибку
#
try:
    raise TypeError('Some message')
except TypeError as e:
    print(e)
#Some message

try:
    print('Fine')
except KeyError:
    print('Nope')
else:
    print('Else clause')
#Fine
#Else clause

try:
    print(1 / 0)
except ZeroDivisionError:
    print('0!')
finally: # finally всегда работает!
    print('I will be called in the end!')
#0!
#I will be called in the end!

try:
    print('try')
except ValueError:
    pass #Игнорирует ошибку!
    print('else')
finally:
    print('finally')


# FUNCTIONS Всегда с маленькой буквы!

def return_none(x):
    print('Param was', x) #Если у функции нет return то она возвращает None!
test = return_none(6)
#Param was 6

print(test)
#None

def sum_numbers(n1, n2, n3):
    print(n1, n2, n3, 'summing...')
    return n1 + n2 + n3

total = sum_numbers(7, 0.3, 0.3)
#7 0.3 0.3 summing...

print(total)
#7.6


def sum_my(a, b=3): # Значение по умолчанию, если аргумент не ввели!
    print(a + b)
# >>> sum_my(1)
#4

#def my_numbers(*args): # Сколь угодно аргументов!

# Class - DICT!
def any_keywords(**kwargs): # Сколь угодно елементов со значением по умолчанию!
    print(kwargs, type(kwargs))

any_keywords(k=1, some=2, wo=3)
#{'k': 1, 'some': 2, 'wo': 3} <class 'dict'>

#CLass - TUPLE. LIST??
def any_keywords(*kwargs): # Сколь угодно елементов со значением по умолчанию!
    print(kwargs, type(kwargs))

any_keywords([1, 2, 3, 4, 5])

#
print('Word', end = '!')
#Word!>>>

print('Word', end = '\n')
#Word
#>>>

#Является ли аргумент функцией? callable()
callable(print)

#Не обязательно ставить "()" у функции, нужно стаить "()" при объявлении и вызове!
def return_min_function():
    return min

test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)

#Глобальные переменные принято называть БОЛЬШИМИ БУКВАМИ: GLOBAL_VAR = []!
#Замыкание - возможность функций использовать чужие переменные!
#Рекурсия - способ функции вызвать саму себя! (Медленная! Лучше циклы!)


print('Max', end='!') #Не переходит на новую строку
print('Max', end='\n')

s, k = (1,2) #Но не s,k,m = (1,2)
print(s,k)
#1 2

first, *second = (1,2,3,4,5)
print(first,second)
#1 [2, 3, 4, 5]

*f,s = 'Moscow'
print(f)
#['M', 'o', 's', 'c', 'o']

def accept_args(*args):
    print(args)
    return sum(args)
print(accept_args(1,2,3,4,5)) #Tuple
values = [1,2,3,4,5] #List
accept_args(values) #Будет ошибка!
accept_args(*values) #Будет работать! Распаковка! Tuple => List

def accept_kwargs(**kawargs):
    print(kawargs)
accept_kwargs(name='Max', job='DBA')
values = {'day':'wed', 'month':'may'}

accept_kwargs(values)#Будет ошибка!
accept_kwargs(**values)#Будет работать! Распаковка! Сколько пар - столько и ключей!
