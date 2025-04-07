value = int(input("введи год "))

if value % 4 == 0 and value % 100 != 0 or value % 400 == 0:
    print("да")
else:
    print("нет")


# введи год 2228
# да


# введи год 1111
# нет


# введи год 1223
# нет

