# Requests
# Документация: [Requests Documentation](https://docs.python-requests.org/en/latest/)
# Основные возможности:
# - Удобный интерфейс для выполнения HTTP-запросов.
# - Поддержка различных методов (GET, POST, PUT, DELETE и др.).
# - Обработка параметров, заголовков и куки.
# - Работа с JSON.

import requests

# Выполняем GET-запрос
response = requests.get('https://api.github.com')
# Проверяем статус-код ответа
if response.status_code == 200:
    print('Данные получены:', response.json())
else:
    print('Ошибка:', response.status_code)






# Matplotlib
# Документация: [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
#
# - Создание статических, анимационных и интерактивных графиков.
# - Поддержка различных типов графиков (линейные, столбчатые, круговые и др.).
# - Настройка внешнего вида графиков (цвета, метки, легенды).

import matplotlib.pyplot as plt

# Данные для визуализации
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создаем линейный график
plt.plot(x, y, marker='o')
plt.title('Простой линейный график')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()



