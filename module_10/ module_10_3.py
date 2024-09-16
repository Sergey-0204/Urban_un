import threading #  используем threading для работы с потоками,
import random  # random для генерации случайных чисел
import time  # и time для задержек.

class Bank:
    def __init__(self): # Конструктор __init__ инициализирует баланс (0) и объект блокировки Lock
        self.balance = 0  # Изначальный баланс
        self.lock = threading.Lock()  # Объект блокировки

    def deposit(self):
        for _ in range(100):  # 100 транзакций пополнения
            amount = random.randint(50, 500)  # Случайная сумма пополнения
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

                # Проверка на разблокировку
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()

            time.sleep(0.001)  # Имитация задержки

    def take(self):
        for _ in range(100):  # 100 транзакций снятия
            amount = random.randint(50, 500)  # Случайная сумма снятия
            print(f"Запрос на {amount}")

            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Блокируем поток, если недостаточно средств

            time.sleep(0.001)  # Имитация задержки

# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
