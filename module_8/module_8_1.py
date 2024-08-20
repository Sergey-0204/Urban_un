def add_everything_up(a, b):
    try:
        # Проверяем, если a и b имеют разные типы
        if isinstance(a, str) and isinstance(b, (int, float)) or isinstance(b, str) and isinstance(a, (int, float)):
            raise TypeError
        # Если оба аргумента - числа, складываем их
        return a + b
    except TypeError:
        # В случае TypeError возвращаем строковое представление a и b
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456,7))          # 130.456