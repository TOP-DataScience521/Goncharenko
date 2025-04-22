#  ==========  4  ==========  

# Написать функцию с именем central_tendency, которая вычисляет основные меры центральной тенденции для некоторого количества чисел.

# Функция принимает обязательными аргументами два вещественных числа и далее произвольное количество вещественных чисел.

#     Два числа должны быть строго позиционными, передаются объектами float.
    
#     Произвольный кортеж позиционных аргументов аннотируется сразу по содержимому. Например, если некоторая функция ожидает произвольное количество целых чисел:
#     >>> def func(*numbers: int):
#     ...     pass

# Функция возвращает словарь с подписанными вычисленными значениями мер центральной тенденции.

def central_tendency(num1: float, num2: float, *rest: float)-> dict[str, float]:   #rest позволяет передать неопределнное колличество позиционных аргументов

   numbers = [num1, num2] + list(rest)   #list() создает список из переданных данных
   sorted_numbers = sorted(numbers)
   lenght = len(numbers)

   median = ( sorted_numbers [ lenght // 2 ]   if lenght % 2 != 0 else sorted_numbers([lenght // 2] + sorted_numbers[(lenght // 2)+1]) /2 )

   arithmetic = round((sum(sorted_numbers)/lenght),1)

# тут вычисляю среднюю геометрическую
   multiplication_num = 1
   for i in numbers:
      multiplication_num = multiplication_num * i
   geometric = round(multiplication_num**(1/lenght), 5)

   harmonic = round(lenght/(sum(1/i for i in numbers)), 5)

   result = {"median": round(median,2), "arithmetic": arithmetic, "geometric": geometric, "harmonic": harmonic}

   return result

print(central_tendency(1,3,5,6,7,8,2,5,1))
# {'median': 5, 'arithmetic': 4.2, 'geometric': 3.33037, 'harmonic': 2.45375}           !!! не смог получить знак после запятой медианы через round
# sample = [1, 2, 3, 4, 5]
# print(central_tendency(*sample))
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.60517, 'harmonic': 2.18978}






#     Ключи словаря:
#         'median' — медиана
#         'arithmetic' — среднее арифметическое
#         'geometric' — среднее геометрическое
#         'harmonic' — среднее гармоническое
    
#     Значения должны быть объектами float. 
#     Округление не использовать.
    
#     Аннотация содержимого словаря осуществляется разными способами. Проще всего обозначить тип всех ключей и тип всех значений. Пример функции, ожидающей словарь с ключами строками и значениями целыми числами:
#     >>> def func(arg: dict[str, int]):
#     ...     pass

# О вычислении приведённых мер центральной тенденции:
#     https://statanaliz.info/statistica/opisanie-dannyx/mediana-v-statistike/
#     https://mateshka.ru/math/arithmetic/srednie-velichini.html
    
#     Взятие корня n-ой степени эквивалентно возведению в степень 1/n

# Примечание: не забывайте про встроенные функции sorted() и sum()

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> central_tendency(1, 2, 3, 4)
#     {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.2133638394006434, 'harmonic': 1.9200000000000004}
#     >>>
#     >>> sample = [1, 2, 3, 4, 5]
#     >>> central_tendency(*sample)
#     {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}