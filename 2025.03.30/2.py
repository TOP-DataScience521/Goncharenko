# Написать программу, которая генерирует форматированную строку.

# Программа в цикле получает из stdin названия фруктов (цикл прерывается при вводе пустой строки).
# Программа выводит в stdout строку с перечислением всех фруктов, добавляя перед последним фруктом союз "и", а перед предыдущими (при их наличии) фруктами добавляя запятые (см. примеры вывода).

# Примечание: идеальным упражнением станет две реализации
#   - получение данных и формирование выходной строки внутри одного цикла
#   - получение данных в одном цикле, затем формирование выходной строки с помощью строковых методов

# Пример ввода 3:
#     яблоко
#     груша
#     апельсин

# Пример вывода 3:
#     яблоко, груша и апельсин

# Пример ввода 4:
#     яблоко
#     груша
#     апельсин
#     лимон

# Пример вывода 4:
#     яблоко, груша, апельсин и лимон

value = input("введите фрукт ")
tuple = []

while True:
    if value  in [""," "]:
        break
    else:
        tuple.append(value)
        value = input("введите фрукт ")

result = ""

for i in tuple:
    if i == tuple[0]:
        result += i
    elif i == tuple[-1]:
        result += f" и {i}"
    else:
        result += f", {i}"

print(result)

# введите фрукт груша
# введите фрукт гуава
# введите фрукт чиа
# введите фрукт киви
# введите фрукт  
# груша, гуава, чиа и киви

# введите фрукт киви
# введите фрукт  
# киви

# введите фрукт киви
# введите фрукт манго
# введите фрукт 
# киви и манго