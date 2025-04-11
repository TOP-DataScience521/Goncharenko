# Написать программу, которая сравнивает две клетки шахматной доски.

# Программа должна по очереди получить из stdin координаты двух клеток шахматной доски (см. пример ввода).
#     По горизонтали клетка кодируется латинскими буквами от ‘a’ до ‘h’.
#     По вертикали клетка кодируется цифрами от 1 до 8.

# Если две заданные клетки покрашены в один цвет, то программа должна вывести в stdout слово “да”. Если клетки покрашены в разные цвета, то должно быть выведено слово “нет”.

# Примечание: в традиционных шахматах клетка а1 всегда чёрного цвета.

# Пример ввода:
#     a1
#     b2

# Пример вывода:
#     да

black = ("a1", "a3", "a5", "a7", "b2", "b4", "b6", "b8", "c1", "c3", "c5", "c7", "d2", "d4", "d6", "d8", "e1", "e3", "e5", "e7", "f2", "f4", "f6", "f8", "g1", "g3", "g5", "g7", "h2", "h4", "h6", "h8")

num1 = str(input("введите координату шахматной доски "))
num2 = str(input("введите координату шахматной доски "))

# num1 = "a2"
# num2 = "b3"

swith1 = 0
swith2 = 0

if num1 in black:
    swith1 = 1
else:
    swith1 = 0

if num2 in black:
    swith2 = 1
else:
    swith2 = 0

if swith1 == swith2:
    print("да")
else:
    print("нет")

# введите координату шахматной доски f1
# введите координату шахматной доски f3
# да

# введите координату шахматной доски a1
# введите координату шахматной доски a2
# нет