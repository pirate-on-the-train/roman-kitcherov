'''
В Python есть 2 вида циклов:
* Целочисленный цикл for
* Условный цикл while
——————————————————————————————————————Цикл for——————————————————————————————————————
Цикл for используется для:
    1. Перебора всех элементов коллекции;
    2. Повтора некоего алгоритма N раз;
Технически, все применения сводятся к перебору всех элементов.
Шаблон:
for ИНДЕКС in КОЛЛЕКЦИЯ:
    Код
    относящийся
    к 
    циклу
    с отступом
ИНДЕКС - это переменная, в которую будут поочерёдно записываться значения КОЛЛЕКЦИИ
КОЛЛЕКЦИЯ - набор из нескольких значений
—————————————————————————————————————Цикл while—————————————————————————————————————
Цикл while используется для:
    1. Повтора алгоритма при соблюдении условия;
    2. Бесконечного цикла;
Шаблон:
while УСЛОВИЕ:
    Код
    относящийся
    к 
    циклу
    с отступом
УСЛОВИЕ - это некое требование или вопрос, который вернёт либо True(Истина), либо False(Ложь)
'''

# for для повтора 10 раз
for i in range(10):
    print('Я учу программирование')

# for для прохода по коллекции 
soup = ['вода', 'мясо', 'картошка', 'лук', 'приправы']
for ingredient in soup:
    print(ingredient)

# for для прохода по диапазону
for i in range(100, 200):
    print(i)

# while для повтора алгоритма, пока условие верно
a = 0
while a < 10:
    a += 1
    print(a)

# while для бесконечного цикла
while True:
    a += 1
    print(a)