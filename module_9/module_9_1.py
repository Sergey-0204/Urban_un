def apply_all_func(int_list, *functions):
    results = {} # Создаем пустой словарь, он будет использоваться для хранения результатов вызовов функций
    for func in functions: # В цикле for мы проходим по всем функциям, которые были переданы в качестве аргументов
        func_name = func.__name__ # Получаем название функции
        results[func_name] = func(int_list)  # Применяем функцию к списку и сохраняем результат
    return results # В конце функция возвращает заполненный словарь.

# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))