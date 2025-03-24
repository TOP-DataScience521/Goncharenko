# Написать программу, преобразовывающую мили в километры.

# Программа должна получить от пользователя целую и дробную часть числа миль за два ввода: см. пример ниже.
# После проведения вычисления необходимо вывести строку с результатами, как в примере ниже. Значение километров должно быть математически округлено до одного знака в десятичной части.

# Используйте следующее соотношение: 1 миля = 1.61 км

# Для округления можно использовать встроенную функцию round(). Информация о её использовании в документации:
#     https://docs.python.org/3/library/functions.html

# Также, для округления можно использовать синтаксис f-строк:
#     >>> f'{12.358:.2f}'
#     '12.36'
#     >>> f'{12.358:.1f}'
#     '12.4'

# Пример ввода:
#     15
#     7

# Пример вывода:
#     15.7 миль = 25.3 км

value_1 = input("Введите первое число") or 3
value_2 = input("Введите второе число") or 21
value = str(value_1)+"."+str(value_2)
float_value = float(value)
miles_per_km = float_value * 1.61

print(f"{value} миль = {miles_per_km} км")

# C:\Users\4surt\OneDrive\Рабочий стол>python 5.py
# Введите первое число 3
# Введите второе число4
 # 3.4 миль = 5.474 км