def all_variants(text):  # функцию - генератор, которая принимает строку text в качестве аргумента
    length = len(text)  # Получаем длину строки
    for start in range(length):  # Проходим по каждому индексу строки
        for end in range(start + 1, length + 1): # Определяем конец подстроки
            yield text[start:end] #  # Возвращаем подстроку от start до end

# Пример использования функции
a = all_variants("abc")
for i in a:
    print(i)