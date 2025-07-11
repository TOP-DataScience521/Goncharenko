# Написать программу, которая проверяет корректность введённого адреса электронной почты.

# Программа получает из стандартного потока ввода (stdin) строку, содержащую адрес электронной почты. 
# Программа выводит в stdout текстовый ответ.

# Для забегающих вперёд: да, такие задачи обычно решаются с помощью регулярных выражений. Но в этой задаче вам необходимо использовать строковые методы:
#     https://docs.python.org/3/library/stdtypes.html#string-methods

# Примечание: в корректном e-mail обязательно есть цифробуквенная последовательность, затем символ '@', затем цифробуквенная последовательность, затем символ '.',
# а затем буквенное имя домена верхнего уровня.
#     Допустимые имена доменов верхнего уровня приведены в файле 1.py

# Примечание 2: цифробуквенными символами в данном случае считаем
#   - буквенные символы всех языков (по UTF-8), а также символы, кодирующие лексемы, включая знаки иных видов письменности (иероглифы, арабская вязь, ...)
#   - символы, кодирующие цифры (арабские, китайские, ...)
#   - символы '_', '.'

# Пример ввода 1:
#     sgd@ya.ru

# Пример вывода 1:
#     да

# Пример ввода 2:
#     abcde@fghij

# Пример вывода 2:
#     нет
high_domains = ['ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bo', 'bq', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'eh', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gb', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mf', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg', 'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'su', 'sv', 'sx', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th', 'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tp', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'um', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ಭಾರತ', '한국', 'ଭାରତ', 'ভাৰত', 'ভারত', 'ישראל', 'বাংলা', 'қаз', 'срб', 'бг', 'бел', 'சிங்கப்பூர்', 'мкд', 'ею', '中国', '中國', 'భారత్', 'ලංකා', 'ભારત', 'भारतम्', 'भारत', 'भारोत', 'укр', '香港', '台湾', '台灣', 'мон', 'الجزائر', 'عمان', 'ایران', 'امارات', 'موريتانيا', 'پاکستان', 'الاردن', 'بارت', 'بھارت', 'المغرب', 'البحرين', 'السعودية', 'ڀارت', 'سودان', 'عراق', 'مليسيا', '澳門', 'გე', 'ไทย', 'سورية', 'рф', 'تونس', 'ລາວ', 'ευ', 'ελ', 'ഭാരതം', 'ਭਾਰਤ', 'مصر', 'قطر', 'இலங்கை', 'இந்தியா', 'հայ', '新加坡', 'فلسطين', 'ye', 'yt', 'za', 'zm', 'zw']

# mail = "sgd@ya.ру"
mail = input("введите эл.почту - ")

revers_mail = mail[::-1]
revers_domein=""

for i in revers_mail:
    if i == ".":
        break
    else:
        revers_domein+=i

domein = revers_domein[::-1]

# print(corentDomein)
if "@" in mail:
  if domein in high_domains:
     print(f"да")
  else:
    print(f"нет")
else:
   print("нет")


# введите эл.почту - sgd@ya.ру
# нет

# введите эл.почту - sgd@ya.ru
# да

# введите эл.почту - asdasdasd.ru
# нет



# def carent_password():
#     # data = input("enter mail - ")
#     data = "awdawd@ada.aad.su"
    
#     if "@" and "." in data:
#         # partition возвращает 3 части списка, до указанного разделителя, сам разделитель и то что после разделителя
#         x = data.partition("@")  
#         part1 = x[0]
#         part2 = x[2].split(".")
#         # разбив на части электронный адрес сможем проверить каждую его часть при необходимости
#         domen = part2[-1]
#         if domen in high_domains:
#             print("da")
#         else:
#            print("no")
#     else:
#         print("no")
#     print(part1)
#     print(part2)
#     print(domen)
        
# carent_password()