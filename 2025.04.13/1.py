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
 
# leaves_count = []

# def tree_leaves(data):
    # def count_leaves(data):
       # global leaves_count
       # for i in data:
          # if isinstance(i, (set, list)):
            # count_leaves(i)
          # elif i == 'leaf':
            # leaves_count.append(i)
    
    # count_leaves(data)
    # print(f"Всего листьев: {len(leaves_count)}")

# tree_leaves(tree)

leaves_count = 0

def tree_leaves(data):
    def count_leaves(data):
       global leaves_count
       for i in data:
          if isinstance(i, (set, list)):
            count_leaves(i)
          elif i == 'leaf':
            leaves_count+=1
    
    count_leaves(data)
    print(f"Всего листьев: {leaves_count}")

tree_leaves(tree)

# 38
