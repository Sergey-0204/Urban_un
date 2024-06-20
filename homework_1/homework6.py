# Работа со словарями:
my_dict = {'Sergey':1985,'Oleg':1984} # Создаём переменную и присваеваем ей словарь из нескольких пар (ключ-значение)
print('Dict:', my_dict) # Вывод словаря на экран
print('Existing value:', my_dict['Sergey']) # значение по существующему ключу
print('Not existing value:', my_dict.get('Vasya'))  # Ключ и значение отсутствует в словаре
print(my_dict) # Вывод словаря на экран
my_dict.update({'Roma': 2006, 'Dima':2011}) # Дабавление  двух пар в словарь
print(my_dict) # Вывод словаря на экран
print('Deleted value', my_dict.pop('Sergey')) # Удаление одной пары в словаре и вывод на экран значения
print('Modified dictionary:', my_dict) # Вывод словаря на экран

# Работа с множествами:
my_set = {100, 500, 9, 100, 500, 'Текст', False, False, (11, 54, 56)} # множество состоящее из разных типов данных
print('set:',my_set) # Вывод на экран уникальных значений (неупорядоченные)
my_set.add(55), my_set.add(True)
print('Modified set:',my_set)