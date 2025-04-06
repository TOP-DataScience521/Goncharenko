value_1 = input("Введите первое число") or 3
value_2 = input("Введите второе число") or 21

# ИСПРАВИТЬ: использование функции str() избыточно
value = str(value_1) + "." + str(value_2)
float_value = float(value)
miles_per_km = float_value * 1.61

# ИСПРАВИТЬ: вывод не соответствует требуемому формату
print(f"{value} миль = {miles_per_km} км")


# Введите первое число 3
# Введите второе число4
#  3.4 миль = 5.474 км


# ИТОГ: 3/5

