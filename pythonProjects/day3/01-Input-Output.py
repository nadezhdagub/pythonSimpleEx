"""
## Ввод/вывод
"""

"""
### Ввод текста в консоли
"""
i = input('num: ')

type(i)

"""
Использование текста
"""
print(i, int(i)*2)

"""
### Форматированый вывод

примеры: безномерной, номерной именованый
"""
i = 1
"I have " + str(i) + " apple"

"I have {} apples and {} bananas".format(3, 2)
"I have {1} apples and {0} bananas".format(3, 2)
"I have {apple} apples and {banan} bananas".format(apple=3, banan=2)

"""
[Полный синтаксис](https://docs.python.org/3/library/string.html#formatspec)

Начиная с версии 3.6 доступен новый синтаксис
Форматирование в виде литералов:
"""
f"I have {i+1} apple."

"""
[Где найти еще примеры]
(https://docs.python.org/3/library/string.html#string.Template.template)

string.Template.template

Старый вариант с использованием процента
"""
"I have %i apples" % 2

"""
### Использование функции [print](https://docs.python.org/3/library/functions.html#print)
```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```
"""
print(1,2,3)
print(1,2,3, sep=';')
print(1,2,3, sep='-', end=';')
print()

"""
Все строки в юникоде
Кодировка входных файлов разная
Строки можно кодировать
"""
"abc абв".encode('cp1251')

"""
и обратно
"""
b'abc \xe0\xe1\xe2'.decode('cp1251')
# 'abc абв'

"""
### Открытие файла

текстовые файлы:
[open](https://docs.python.org/3/library/functions.html#open)
 открывает файл и возвращает "файл-подобный" объект
"""
f = open("day3/examples/fox.txt")
type(f)

"""
### Открытие файла с кодировкой

Можно указать кодировку при чтении/записи в текстовом режиме
"""
f = open("day3/examples/citrus-1251.txt", encoding="cp1251")
# чтение строки
f.readline()
# чтение всего файла в одну строку
f.read()
f.seek(0)
# чтение в список
f.readlines()

"""
закрытие файла, когда он больше не нужен
"""
f.close()

f = open("day3/examples/citrus-utf8.txt", encoding="utf8")
f.readline()
f.close()

"""
работа с каждой строкой
"""
for line in open("day3/examples/fox.txt"):
   print(line.strip())

"""запись в файл
"""
f = open("test.txt", "w")  # "w" - создать файл для записи
f.write("Тест\n")              # записать в file-подобный объект
f.write("проверка")

"""
печать в файл
"""
print("text", file=f)
f.close()

"""
менеджер контекста
"""
with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')

"""
загрузка из бинарного файла
"""
fb = open("day3/examples/citrus-1251.txt", "rb")
citrus=fb.read()
print(citrus.decode(encoding='cp1251'))
fb.close()


fb = open("testw.txt", "wb")
fb.write(b'hello')
fb.write("Привет".encode("cp1251"))
fb.close()