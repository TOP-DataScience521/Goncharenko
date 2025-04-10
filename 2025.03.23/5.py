# Написать программу, которая подсчитывает стоимость отправки телеграммы.

# В прошлом веке для отправки коротких текстовых сообщений люди использовали телеграммы. В разное время их стоимость рассчитывалась по-разному.
# Но при передаче телеграмм по ключу (морзянкой) стоимость отправки телеграммы зависит от количества знаков. 
# В нашей задаче примем, что один символ буквы или цифры стоит тридцать копеек.

# Программа получает из stdin строку с текстом телеграммы.
# Программа выводит в stdout стоимость в рублях и копейках, согласно формату в примере ниже.

# Пример ввода:
#     грузите апельсины бочках братья карамазовы

# Пример вывода:
#     11 руб. 40 коп.

price = 0.30
# print(type(price))

text = input("введите текст - ")
carent_text = text.replace(" ","")
cost = price * len(carent_text)
format_cost = "{:.2f}".format(cost)

print(f"{format_cost[:-3]} руб. {format_cost[-2:]} коп.")

# введите текст - грузите апельсины бочках братья карамазовы!!!
# 12 руб. 30 коп.
