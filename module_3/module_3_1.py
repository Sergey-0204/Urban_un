
calls = 0  # Количество вызовов


def count_calls():  # Функция подсчета вызовов
    global calls
    calls += 1


def string_info(string):  # Функция для получения информации о строке
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):  # Функция для проверки наличия строки в списке строк, без учета регистра
    count_calls()
    string_lower = string.lower()
    list_to_search_lower = [item.lower() for item in list_to_search]
    return string_lower in list_to_search_lower

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
