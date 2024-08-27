first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, где длина строки не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список кортежей пар слов одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Словарь с парой ключ-значение, где длина строки четная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)