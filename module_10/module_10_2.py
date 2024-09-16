import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power): # Конструктор __init__ принимает имя и силу рыцаря, и инициализирует общее количество врагов (100) и счетчик дней.
        super().__init__()
        self.name = name # Имя
        self.power = power # Сила
        self.enemies = 100  # Общее количество врагов
        self.days = 0 # счетчик дней

    def run(self): # выполняет основную логику сражения
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день сражения)
            self.days += 1 #  В цикле уменьшает количество врагов на значение power каждые 1 секунду, увеличивая счетчик дней
            self.enemies -= self.power

            if self.enemies < 0:
                self.enemies = 0 # Если количество врагов становится отрицательным, оно устанавливается в 0

            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения всех потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании битв
print("Все битвы закончились!")