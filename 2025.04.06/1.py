#   ==========  1  ==========  

# Написать функцию с именем strong_password, которая проверяет, является ли пароль надёжным.

# Функция принимает обязательным позиционно-ключевым аргументом пароль в виде объекта str.

# Функция возвращает объект bool.

# Пароль считается надёжным, если соблюдены все нижеследующие условия:
#     - длина пароля составляет восемь символов и более
#     - в пароле присутствуют буквенные символы в обоих регистрах
#     - в пароле присутствуют минимум два символа цифр
#     - кроме символов букв и цифр в пароле присутствуют символы прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.)

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> strong_password('aP3:kD_l3')
#     True
#     >>> strong_password('password')
#     False
control = "., :;'!%&*`"
remov_str = "0123456789"

def strong_password(str):

    count_num = 0                  # для проверки на наличие 2ух цифр
    is_lower = False   
    is_upper = False
    is_symbol = False

    result_str = "".join([char for char in str if char not in remov_str]) #обрезаю цифры (как понял то пайтон "0123456789" воспринимает как нижний регистр и их нужно ставить в итерацию по lowerCase)

    if len(str) > 8:
        for i in str:
            if i in remov_str:
                count_num+=1
            if i in control:      #проверка на символы
                is_symbol = True
        for i in result_str:
            if i == i.lower():    #проверка на lowerCase
                is_lower = True
            if i == i.upper():    #проверка на upperCase
                is_upper = True
        if count_num >=2 and is_lower == True and is_symbol == True and is_upper == True:
            return True
    return False
        


# result = ''.join([char for char in main_str if char not in to_remove])
# Используется генератор списка, который проходит через каждый символ в main_str. Символ добавляется в результат только тогда, когда он не содержится в строке to_remove.
# Метод ''.join() соединяет итоговый список символов обратно в строку.
    
print(strong_password("password!"))
# False

# print(strong_password("aaaaaAAA112!"))
# # True