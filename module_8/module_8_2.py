def personal_sum(numbers):  # Функция с параметром содержащий элементы, которые мы хотим сложить
    result = 0  # инициализируется нулем и будет хранить сумму корректных чисел
    incorrect_data = 0  # количество некорректных данных

    for item in numbers: # Цикл проходит по каждому элементу
        try:
            result += float(item)  # Пытаемся преобразовать элемент в float и добавляем его к result
        except (TypeError, ValueError): # Тип ошибки
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1  # Увеличиваем счетчик некорректных данных на единицу

    return result, incorrect_data  # Функция возвращает кортеж, содержащий сумму всех корректных чисел (result) и количество некорректных данных (incorrect_data).


def calculate_average(numbers): # Функция №2
    try:  # Проверяем, является ли numbers списком или кортежем. Если нет, вызываем исключение TypeError
        if not isinstance(numbers, (list, tuple)):
            raise TypeError
        total_sum, incorrect_count = personal_sum(numbers) # Вызываем функцию personal_sum, которая возвращает сумму корректных чисел и количество некорректных данных.
        count = len(numbers) - incorrect_count

        return total_sum / count if count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры использования
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
