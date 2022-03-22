"""
## Исключения

### Назначение исключений

- Обработка ошибок
- Уведомления о событиях
- Обработка особых ситуаций
- Заключительные операции

### Использование исключений
"""
try:
#    raise SyntaxError("My syntax error")
    #Nones # NameError
#    1 + "2" # TypeError
    [1,2][3] # IndexError
    print("All fine")
except NameError:
    print("Name error.")
except IndexError as ie:
    print("Index error:", ie)
except (AttributeError , TypeError) as e:
    print("AttributeError or TypeError!!!")
else: # Выполняется, если не было исключений.
    print ("In else block")
finally: # Этот блок выполняется всегда.
    print ("In finally block")



try:
    with open('file.txt') as f:
        f.read()
except FileNotFoundError as err:
    print('file not found')

"""
### Объекты исключений

Исключение без параметров

Обязательное наследование от Exception
"""
class Simple(Exception):
    def __str__(self):
        return "I am simple exception"

try:
    raise Simple
    #raise Simple() # можно вызвать и так
except Simple as s:
    print("Simple error: ", s)

"""
Исключение с параметром
"""
class General(Exception):
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return "I am general exception {}".format(self.v)

try:
    raise General('bad')
except General as e:
    print("Oh no!!! General error!!! -> {}".format(e))
except Exception as e:
    print(e)

"""
### Программная генерация исключения assert
"""
try:
    assert 1 > 2, "Error"
except AssertionError as g:
    print("Assett error: ", g)
    raise

"""
Стандартные исключени и иерархия классов

[Стандартные исключения](https://docs.python.org/3/library/exceptions.html)

[Иерархия стандартных исключений](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
"""