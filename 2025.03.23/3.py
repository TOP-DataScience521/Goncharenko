# Написать программу, которая вычисляет сумму всех делителей числа.

# Программа получает из stdin натуральное число. 
# Далее, программа считает и выводит в stdout сумму делителей этого числа.

# Необходимо использовать цикл с минимально возможным количеством итераций.

# Пример ввода:
#     50

# Пример вывода:
#     93

number = int(input("inter number "))
tuple = []
i = 1

while i <= number:
    if number % i == 0:
        tuple.append(i)
        i+=1
    else:
        i+=1
# print(tuple)

sum = 0
j = 0
while len(tuple) > j:
    sum += tuple[j]
    j+=1

print(sum)

# inter number 12
# 28

# inter number 100
# 217