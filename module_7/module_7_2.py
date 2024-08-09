
def custom_write(file_name, strings): #  Фунция с двумя аргументами.
    strings_positions = {} #  Cловарь, который используется для хранения информации о позициях записанных строк в файле.

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1): # Используем enumerate для перебора строк с индексацией, начиная с 1
            # Получаем текущее положение в файле (байты)
            byte_position = file.tell()
            # Записываем строку в файл с символом новой строки
            file.write(string + '\n')
            # Сохраняем информацию о позиции и строке в словаре
            strings_positions[(index, byte_position)] = string

    return strings_positions # Функция возвращает словарь


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Вывод результата на консоль, возвращает представление всех пар ключ-значение в словаре result
for elem in result.items():
    print(elem)