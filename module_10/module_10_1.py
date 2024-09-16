import threading
from time import sleep, time # Импортируем необходимые модули для работы с потоками и для задержки и измерения времени.

def write_words(word_count, file_name): # Принимает количество слов и имя файла.
    with open(file_name, 'w') as f: # Открывает файл для записи
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово №{i}\n")
            sleep(0.1)    # Записывает слова в файл с задержкой 0.1 секунды между записями.
    print(f"Завершилась запись в файл {file_name}") # После завершения записи выводит сообщение о завершении


start_time = time() # Измеряем время выполнения функции

# Вызов функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Измеряем время выполнения потоков
start_time = time()

# Создание потоков
threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for args in thread_args:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

end_time = time()
print(f"Работа потоков {end_time - start_time:.6f} секунд")