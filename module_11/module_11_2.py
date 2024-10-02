def introspection_info(obj):
    """
    Функция для проведения интроспекции объекта и возвращения его типа, атрибутов,
    методов, модуля и других свойств.

    Args:
        obj: Объект для интроспекции.

    Returns:
        Словарь с информацией об объекте.
    """
    # Инициализируем словарь для хранения информации об объекте
    info = {'type': type(obj).__name__, 'module': type(obj).__module__}

    # Получаем тип объекта

    # Получаем модуль, к которому принадлежит объект

    # Списки для хранения атрибутов и методов
    attributes = []
    methods = []

    # Итерация по всем атрибутам объекта
    for attr_name in dir(obj):
        # Получаем значение атрибута
        attr_value = getattr(obj, attr_name)

        # Проверяем, является ли атрибут вызываемым (т.е. методом)
        if callable(attr_value):
            methods.append(attr_name)
        else:
            attributes.append(attr_name)

    # Добавляем атрибуты и методы в словарь
    info['attributes'] = attributes
    info['methods'] = methods

    # Возвращаем собранную информацию
    return info

# Пример использования:
number_info = introspection_info(42)
print(number_info)