## Области видимости

[LEGB Rule.](https://docs.python.org/3/reference/executionmodel.html#resolution-of-names)

* L. Local.
* E. Enclosing function locals.
* G. Global (module)
* B. Built-in (Python)

вложеные функции
"""
x = 1
def outer(a):
        b = 2
        def inner(c):
                d = 3
                print("a=", a)
                print("b=", b)
                print("c=", c)
                print("d=", d)
                print("x=", x)
        return inner

i = outer(5)
i(6)

"""
### Инструкция global
"""
def fun_not_global():
        x = 2

def fun_global():
        global x
        x = 2

x = 1
print(x)
fun_not_global()
print(x)

fun_global()
print(x)

"""
### nonlocal
"""
b=2
def outer(a):
        b = 1
        def inner(c):
                nonlocal b
                b = 2
        inner(5)

"""
### Изменяемые аргументы как параметры функций
"""
def f1(l: list):
    l.append(3)

def f2(l):
    l = [3]

arg = [2]
f1(arg)
print(arg)
f2(arg)
print(arg)

arg = 1
# Генерируется ошибка т.к. несовместимый параметр
f1(arg)

"""
### Область видимости для изменяемых значений

Коварное присваивание

Это работает
"""
x = 10
def bar():
    print(x)
bar()

"""
это выдает исключение
"""
x = 10
def foo():
    print(x)
    x = x + 1
foo()

"""
исправление ситуации
"""
x = 10
def foobar():
    global x
    print(x)
    x = x + 1

foobar()