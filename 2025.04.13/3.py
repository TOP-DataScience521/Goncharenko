  # ==========  3  ==========  дополнительно
# Написать рекурсивную функцию с именем tree_generator, которая генерирует дерево с произвольным количеством веток и листьев.
# Вложенность веток также должна быть произвольной.
# Функция не принимает аргументы.  
    # Роль листа должна играть строка 'leaf'.
# Функция возвращает объект list.
    # Добейтесь такого поведения, чтобы возвращаемый список не мог быть пустым, но вложенные списки (ветки) могли.
# Примечание: используйте функцию randrange() из модуля random стандартной библиотеки.
# Работу написанной функции необходимо проверить.
# Пример проверки:
    # >>> tree_generator()
    # [[], ['leaf'], [[[[]], [['leaf'], [['leaf', 'leaf', 'leaf']], ['leaf']], [[]], ['leaf']], ['leaf', 'leaf']], [[[]], [[], [[['leaf']], [['leaf', 'leaf']], ['leaf'], [['leaf', 'leaf', 'leaf'], [[], ['leaf', 'leaf', 'leaf'], [[['leaf', 'leaf', 'leaf'], [], [[], ['leaf']], ['leaf', 'leaf', 'leaf']], ['leaf', 'leaf', 'leaf'], [['leaf']], []], ['leaf']], ['leaf'], ['leaf'], []]], [['leaf'], ['leaf', 'leaf', 'leaf']], ['leaf', 'leaf']], ['leaf', 'leaf', 'leaf']], ['leaf']]
    # >>>
    # >>> tree_generator()
    # [[[['leaf']]], []]
from random import *

def tree_generator():
    x ="leaf"
    list_leaf = []
    range_generate = randrange(0,5)
    random_num = randrange(0,10)
    
    for i in range(range_generate):
        if random_num <= 3:
            list_leaf.append(tree_generator())
        elif random_num >= 7:
            leaf_str = ",".join([x]*randrange(1,4))
            list_leaf.append([leaf_str])
        else:
            leaf_str = ",".join([x]*randrange(1,4))
            list_leaf.append(leaf_str)
    return list_leaf    
        
print(tree_generator())

