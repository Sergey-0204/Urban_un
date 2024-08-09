import re


class WordsFinder:
    def __init__(self, *file_names):  # принимает неограниченное количество названий файлов и сохраняет их в  file_names
        self.file_names = file_names

    def get_all_words(self):  # Метод get_all_words
        all_words = {}  # Создает пустой словарь all_words
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file: # Перебирает названия файлов, открывает каждый файл и считывает его содержимое
                    content = file.read().lower() # Приводит текст к нижнему регистру
                    content = re.sub(r"[',.!?;:-]", '', content)  # Убираем пунктуацию
                    words = content.split()  # Разбиваем на слова
                    all_words[file_name] = words  # Сохраняем слова в словаре
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")

        return all_words

    def find(self, word):
        word = word.lower() #  Приведение к нижнему регистру
        result = {} # Создание пустого словаря
        all_words = self.get_all_words() # возвращает все слова

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # +1 для 1-индексации
        return result

    def count(self, word): # Метод count
        word = word.lower() #  Приведение к нижнему регистру
        result = {} # cоздание пустого словаря
        all_words = self.get_all_words() # возвращает все слова

        for file_name, words in all_words.items():
            result[file_name] = words.count(word) # Считаем количество вхождений слова в каждом файле
        return result # Возврат результата


# Пример использования
finder = WordsFinder('test_file.txt')
# finder = WordsFinder('test_file2.txt')
# finder = WordsFinder('test_file3.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))  # Позиция первого слова
print(finder.count('teXT'))  # Количество слов