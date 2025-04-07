# value = input("введите цифру больше нуля ")
# int_val = int(value)
# if not value.isdigit():
#     print("не является числом")
# elif int(value) % 2 == 0 and int(value) != 6:
#     print("да")
# else:
#     print("нет")


try:
    value = int(input("введите цифру больше нуля "))
except ValueError:
    print("не является числом")
else:
    if 0 < value % 2 == 0 and value != 6:
        print("да")
    else:
        print("нет")


# введите цифру больше нуля 2
# да


# введите цифру больше нуля asd
# не является числом


# введите цифру больше нуля 5
# нет


# введите цифру больше нуля -8
# нет

