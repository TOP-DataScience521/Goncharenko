# Написать программу, которая принимает пользовательский ввод только до тех пор пока он соответствует условию.

# Программе в цикле получает из стандартного потока ввода (stdin) по одному целому числу, кратному семи. При появлении любого числа, не делящегося на семь, цикл прерывается. 
# После окончания цикла программа выводит в stdout в одну строку все числа кратные семи в обратном порядке.

# Пример ввода:
#     7
#     7
#     14
#     21
#     13

# Пример вывода:
#     21 14 7 7

array = []

num = input("inter number ")

while int(num) % 7 == 0:
    array.append(num)
    num = input("inter number ")

sort_array = ""
i = len(array)
while i > 0 :
    sort_array += (array[i-1]+ " ")
    i-=1

print(sort_array)

# inter number 7
# inter number 7
# inter number 14
# inter number 21
# inter number 13
# 21 14 7 7 