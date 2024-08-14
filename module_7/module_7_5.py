import os
import time # Импортируем необходимые модули os и time

# Устанавливаем переменную directory равной ".", что означает текущую директорию.
directory = "."

# Обход каталога
for root, dirs, files in os.walk(directory): # Используем os.walk(directory) для обхода всех подкаталогов и файлов в указанной директории
    for file in files:   # перебирает все файлы в текущем каталоге
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Форматируем строку с информацией о каждом найденном файле и выводим её на экран
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')