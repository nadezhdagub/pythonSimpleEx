"""
## Функции

# Определение функции

[Функции](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
### Документирование
"""
def fun1(arg1, arg2):
    """
    :param arg1:
    :param arg2:
    :return:
    """
    print(arg1, arg2)

fun1('hello', 'world')

"""
Начиная с версии 3.5 можно опциально описывать типы
входящих данных и тип возвращаемого значения
"""
def fun_with_types(i: int, s: str) -> bool:
    return s[i] == 'a'


fun_with_types(1, "ddd")
   
"""
Но все так же можно передавать любые типы
"""
fun_with_types(1, ['a', 'a'])

"""
Для статической проверки типов используется пакет mypy


### Переменное количество аргументов
"""
def fun2(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
    if args:
        print("args[0]: {}".format(args[0]))
    if kwargs:
        print("kwargs['parameter']: {}".format(kwargs.get('parameter')))

fun2(1, 2)
fun2(1, 2, 3 ,4)
fun2(1, 2, 3 ,4, parameter=1)
fun2(1, 2, 3 ,4, param=1)

"""
### Значения по умолчанию
"""
def fun3(a, d=1):
    print(a, d)

fun3(1)
fun3(1, 2)

"""
### Именованные параметры
"""
fun3(d=3, a=4)

"""
### Упаковка и распаковка параметров

- *args
- **kwargs
"""
def fun4(a, *args):
    print(a, args)
    if args:
        print("args[0]: {}".format(args[0]))

l = [1, 2, 3]

"""
### Распаковка списка при вызове функций
"""
fun4(1, 2, *l)
fun4(1, 2, l)
fun4(1, 2, 1, 2, 3)


def fun5(a, b, c):
    print(a, b, c)

fun5(*l)

"""
### Возвращаемое значение по умолчанию
"""
def default():
    pass

print(default())

"""
### Возвращение нескольких значений
"""
def mulret():
    return 1, 2, 3

print(mulret())
a, b, c = mulret()
print(a, b, c)

"""
### Замыкания
"""
def outer(a):
        def inner(c):
                return a + c
        return inner

closure = outer(1)
closure
print(closure(2))

"""
### lambda
"""
lambda x, y: x + y + 1
adder = lambda x: x + 1
adder(2)

"""
допускается создание идентификаторов на русском языке, но лучше так не делать.
"""
список = [(1, 3), (2, 2), (3, 1)]
sorted(список, key=lambda i: i[1])

"""
### [Встроенные функции]
(https://docs.python.org/3/library/functions.html?highlight=builtin%20functions)
"""
min(1, 2)
max([1, 4, 6, 3])

"""
#### Параллельный обход: zip
"""
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
zip(L1, L2)
list(zip(L1, L2))
dict(zip(L1, L2))

for x, y in zip(L1, L2):
    print(x, '+', y, '=', x + y)

"""
### Функциональные инструменты
#### Генераторы списков и функция map
"""
help(ord)
m = map(ord, 'spam')
list(m)
L = 'spam'
[ord(i) for i in L]

"""
#### Функция filter
"""
L = [1, 0, None, True, 2]
list(filter(bool, L))
[i for i in L if i]

"""
#### Функция any
"""
L = [True, None, 1]
any(L)

"""
#### Функция all
"""
all(L)

"""
### Функции высшего порядка
# map, filter
"""
obj = map(lambda x: x * x , [1, 2, 3, 4, 5])
[x * x for x in [1,2]]

l = [1, 2, 3, 4, 5]
list(filter(lambda x: x%2, l))


def superfun(fun, arg1, arg2):
        return fun(arg1, arg2)

superfun(min, 1, 2)
superfun(max, 1, 2)

"""
### [Модуль functools]
(https://docs.python.org/3/library/functools.html)

Инструменты для функционального программирования
- partial
- lru_cache
- cache (c версии 3.9)
"""
from functools import lru_cache

@lru_cache
def cache(i):
    print(f'-{i}-')

cache(1)
cache(2)
cache(1)


@lru_cache
def fibonachi(i):
    if i < 3:
        return 1
    return fibonachi(i - 1) + fibonachi(i - 2)
fibonachi(100)


def fibonachi_nocache(i):
    if i < 3:
        return 1
    return fibonachi_nocache(i - 1) + fibonachi_nocache(i - 2)
# !! Если запустить с большим значением (больше 35), ждать придется очень долго
fibonachi_nocache(33)


"""
[partial](https://docs.python.org/3/library/functools.html#functools.partial)
"""
from functools import partial

def greeting(prefix, name):
    print(prefix, name)

hello = partial(greeting, "Hello, ")
goodbye = partial(greeting, "Goodbye, ")

hello('Peter')
goodbye('Mike')

"""
### [Модуль operators]
(https://docs.python.org/3/library/operator.html)

Стандартные операции в виде функций
(замена простым lambda)
"""
from functools import  reduce
from operator import mul, add

reduce(mul, [1, 2, 3, 4, 5])
reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

reduce(add, [1, 2, 3, 4, 5])
