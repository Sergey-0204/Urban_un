
def print_params(a=1, b='строка', c=True): # функция которая принимает три параметра
    print(a, b, c)

# Вызовы функции print_params с разным количеством аргументов
print_params()    # вызов без аргументов
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2.Распаковка параметров:
values_list = [99, 'hello', False]
values_dict = {'a': 66, 'b': 'world', 'c': True}
print_params(*values_list)  # *Список
print_params(**values_dict)  # **Словарь

# 3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)