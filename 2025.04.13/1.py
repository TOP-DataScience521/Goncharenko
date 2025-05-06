#   ==========  1  ==========  

# Написать рекурсивную функцию с именем tree_leaves, которая считает количество листьев на дереве.

# Функция принимает обязательным позиционно-ключевым аргументом список веток дерева.
    
#     Роль листа будет играть строка 'leaf'.
#     Каждая ветка дерева может содержать вложенные ветки и листья. То есть элементами исходного списка могут быть строки (листья) и списки (ветки),
#  которые в свою очередь могут содержать как листья, так и строки (см. пример проверки).
    
#     Поскольку речь идёт о произвольной структуре данных, то в аннотации параметра функции тип элементов не указывается.

# Функция возвращает объект int.

# Работу написанной функции необходимо проверить.

# Пример проверки:
#     >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']],
#  [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'],
#  ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
#     >>> 
#     >>> tree_leaves(tree)
#     38
tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']],
 [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'],
 ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]


def tree_leaves(data):
    result = []
    
    for i in data:
        if type(i) in (tuple, list, dict, set):
            result.extend(tree_leaves(i))     # тут выдает ошибку о неитерируемом объекте, не смог разобраться в этой ситуации, через ретёрн работает, а если применить len внутри функции то ошибка
        elif i == "leaf":
            result.append(i)
    return result

print(len(tree_leaves(tree)))

# 38
