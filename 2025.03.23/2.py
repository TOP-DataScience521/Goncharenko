# Написать программу, которая подсчитывает сумму введённых положительных чисел.

# Программа получает из stdin натуральное число n. Затем получает из stdin по очереди n целых чисел.
# Сумму положительных чисел из введённых программа выводит в stdout.

# Пример ввода:
#     6
#     3
#     -5
#     1
#     10
#     -1
#     8

# Пример вывода:
#     22
tuple = []

count = int(input("inter count  "))
i = 0
sum = 0

while i < count:
    number = input("inter number  ")
    i+=1
    tuple.append(int(number))

for n in tuple:
    if n > 0:
        sum+=n

print(sum)

# inter count  4
# inter number  4
# inter number  1
# inter number  -3
# inter number  2
# 7