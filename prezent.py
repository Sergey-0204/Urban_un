import matplotlib.pyplot as plt
import numpy as np

# Данные
municipal_districts = ['Балашиха', 'Богородский', 'Восход', 'Жуковский', 'Клин', 'Коломна', 'Королев' ]
connected = [0, 33, 1, 36, 35, 7, 0]
not_connected = [36, 3, 35, 0, 1, 29, 36]

x = np.arange(len(municipal_districts))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 6))

# Создание столбцов
ax.bar(x, connected, width, label='Подключено', color='green')
ax.bar(x, not_connected, width, bottom=connected, label='Не подключено', color='red')

# Настройка осей и заголовка
ax.set_ylabel('Всего количество ноутбуков')
ax.set_title('Подключение образовательных организаций по городским округам')
ax.set_xticks(x)
ax.set_xticklabels(municipal_districts, rotation=45)
ax.legend()

# Добавление подписей данных
for i in range(len(municipal_districts)):
    ax.text(x[i], connected[i]/2, connected[i], ha='center', va='center', color='white', fontsize=10)
    ax.text(x[i], connected[i] + not_connected[i]/2, not_connected[i], ha='center', va='center', color='white', fontsize=10)

plt.tight_layout()
plt.show()