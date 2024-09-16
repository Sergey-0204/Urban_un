import random
import time
from threading import Thread
from queue import Queue

class Table:  # Хранит номер стола и информацию о госте, который за ним сидит
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость за столом (по умолчанию None)

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self): # Наследуется от Thread. В методе run происходит задержка от 3 до 10 секунд, имитируя время, проведенное за столом.
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)

class Cafe:
    def __init__(self, *tables):  # Управляет столами и очередью
        self.queue = Queue()  # Очередь для ожидания гостей
        self.tables = tables   # Список столов

    def guest_arrival(self, *guests): # принимает гостей и размещает их за столами или ставит в очередь
        for guest in guests:
            # Ищем свободный стол
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest  # Сажаем гостя за стол
                guest.start()  # Запускаем поток
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)  # Помещаем в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self): # обслуживает гостей, освобождая столы и перемещая гостей из очереди
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    # Проверяем очередь на наличие ожидающих гостей
                    if not self.queue.empty():
                        next_guest = self.queue.get()  # Берем следующего из очереди
                        table.guest = next_guest
                        next_guest.start()  # Запускаем поток
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()