print(int('1'))

"""
### Инструкции
"""
a = 1
b = 2
print(a, b)

"""
Несколько специальных случаев
"""
a = 1; b = 2; print(a, b)

"""
### Присваивание
"""
a = 1
b = 2
a, b = b, a
c, *d = 'good', 'ugly', 'bad'
print(c, ':', d)

"""
### Длинные строки

Обратный слеш в конце строки
"""
very_very_very_long_variable_name = \
    2
"""
но лучше использовать скобки
"""
very_very_very_long_variable_name2 = (
    2
    +
    2)

"""
### [Встроенные ключевые слова]

`import, def, class, if, for, while` и др.

"""
if a == 1 or b == 2:
    print(1)
elif a == 2:
    print(2)
else:
    print(3)
    print(5)

print(4)

"""
#### Трехместное выражение if/else
"""
a = True
A = 'Y' if a else 'Z'
A

a = False
A = 'Y' if a else 'Z'
A

print('Result of if:', 'Y' if a else 'Z')


True and False
True or False
not True

state1 = True
state2 = False
result = state1 and state2
print(result)

current = None
default = "Name"
result = current or default
print(result)

"""
Допустимо записывать одну инструкцию в нескольких строках
"""
c = 1
d = 2
if (a == 1 and
    b == 2 and
    c == 3 and
    d == 4):  # Не забываем про двоеточие
    print('spam ' * 3)

"""
Тело инструкции в одной строке
"""
if a < b: print(c)


a = 10
while a > 0:
    a -= 1

"""
`break, continue, pass, else`
"""
while a > 1:
    a = a - 1
    if a % 2:
        continue  # Перейти в начало циклa
    result = id(a)
    if result:
        break  # Выйти из цикла, пропустив часть else
else:  # Выполняется, если _не_ была использована инструкция 'break'
    print("bad action")

"""

простой вариант
"""
for i in range(5, 10, 2):
    print(i)

"""
полный вариант
"""
for i in range(10):  # Присваивает элементы объекта с переменной цикла
    res = id(i)
    if res > 0: break  # Выход из цикла, минуя блок else
    if res < 0: continue  # Переход в начало цикла
else:
    print("good")  # Если не была вызвана инструкция 'break'

"""
### Приемы программирования циклов
#### Счетные циклы:  range
"""
list(range(5))
list(range(10, 20))
list(range(5, 30, 7))
for i in range(3):
    print(i, ' Pythons')

"""
#### Генерирование индексов и элементов: enumerate
"""
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'at offset', offset)

"""
Сортировка последовательностей

"""
origin = 'avdsdf'
sorted(origin)
#['a', 'd', 'd', 'f', 's', 'v']

origin

"""
Сортировка массива

"""
origin = [3, 1, 2]
origin.sort()
origin

"""
Удобный поиск подстроки
Или элемента в массиве
"""
s = 'spam'
'm' in s
1 in [0, 1, 2]


"""
### Менеджер контекста

"""
with open('day2/02-Syntax.py', encoding='utf8') as myfile:
    content = []
    for line in myfile:
        content.append(line)
    print(len(content))

"""
### Итераторы

Для унификации работы с последовательностями создан специальный протокол.
Например все, что используется в операторе 'for' справа от 'in' является итератором
"""
I = [1, 2]
I = (1, 2)
I = {1, 2}
I = {"1": 3, "2": 4}
I = "I'am iterator"

"""
работа с элементами  с помощью цикла
"""
for l in I:
    print(l)

"""
### Генерация последовательностей

Создание списков в виде инструкции
"""
L = [i for i in range(5)]
"""
то же самое в виде цикла
"""
L = []
for i in range(5):
    pass



"""
список нечетных чисел
"""
L = [i for i in range(10) if i % 2]

L = []
for i in range(5):
    if i % 2:
        L.append(i)

"""
множество:
"""
{i for i in range(5)}

"""
словарь:
"""
{i: i + 1 for i in range(5)}

d = {}
for i in range(5):
  d[i] = i + 1

"""
Похоже на создание последовательностей в виде литералов
сравните:
"""
[0, 1, 2]
[i for i in range(3)]

{0, 1, 2}
{i for i in range(3)}

{0:1, 1:2, 2:3}
{i: i + 1 for i in range(3)}

"""
Выражения-генераторы реализация "ленивых" вычислений
"""
(i for i in range(5_000_000))

