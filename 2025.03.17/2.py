num1 = int(input("введите первое число  "))
num2 = int(input("введите второе число  "))
    
if num1 % num2 == 0:
    print (f"{num1} делится на {num2} нацело\nчастное: {num1 // num2}")
# ИСПРАВИТЬ: проверка связана с предыдущей, значит должна быть частью одной условной инструкции
# исправил на else
else:
    # ИСПРАВИТЬ: одинаковые операции в большинстве случаев имеет смысл выполнить заранее
    print (f"{num1}  не делится на {num2} нацело\nнеполное частное: {num1 // num2}\nостаток: {num1 % num2}")

    
# введите первое число  6
# введите второе число  2
# 6 делится на 2 нацело
# частное: 3


# введите первое число  9
# введите второе число  2
# 9  не делится на 2 нацело
# неполное частное: 4
# остаток: 1


# ИТОГ: 2/4

