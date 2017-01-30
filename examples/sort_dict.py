my_dict = {'a': 3, 'c': 1, 'b': 2}

# Упорядочим элементы словаря по ключам.
sorted(my_dict.items(), key=lambda item: item[0])  
# [('a', 3), ('b', 2), ('c', 1)]

# Упорядочим элементы словаря по значениям.
sorted(my_dict.items(), key=lambda item: item[1])  
# [('c', 1), ('b', 2), ('a', 3)]
