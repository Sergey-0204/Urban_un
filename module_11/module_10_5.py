import time
from multiprocessing import Pool


def read_info(name):  # Определяем функцию read_info, которая будет считывать содержимое файла.
    all_data = []  # Инициализирует пустой список для хранения прочитанных строк.
    with open(name, 'r') as f: # Открывает файл в режиме чтения
        while True: # Бесконечный цикл для считывания строк
            line = f.readline() # Считывает одну строку из файла.
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список



if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)] # Создает список имен файлов.

    # Линейный вызов
    start_time = time.time() # Записываем текущее время перед началом считывания.
    for filename in filenames: # последовательно вызывает функцию read_info для каждого файла.
        read_info(filename)
    linear_time = time.time() - start_time
    print(f'{linear_time:.6f} (линейный)') # После завершения считывания вычисляется общее время выполнения и выводится на экран

    # Многопроцессный вызов
    start_time = time.time() # Записываем текущее время перед началом считывания.
    with Pool() as pool: # Создает пул процессов. По умолчанию количество процессов равно количеству доступных ядер процессора.
        pool.map(read_info, filenames) # Распределяет список файлов между процессами, вызывая функцию read_info для каждого файла параллельно.
    multiprocessing_time = time.time() - start_time
    print(f'{multiprocessing_time:.6f} (многопроцессный)') # После завершения считывания вычисляется общее время выполнения и выводится на экран
