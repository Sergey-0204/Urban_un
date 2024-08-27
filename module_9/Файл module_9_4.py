first = 'Мама мыла раму'
second = 'Рамена мало было'

#  Используется map для применения lambda-функции к каждой паре символов из строк first и second.
#  Функция возвращает True, если символы совпадают, и False в противном случае.
result = list(map(lambda x, y: x == y, first, second))

print(result)  # Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]



def get_advanced_writer(file_name):  # Функция get_advanced_writer создает внутреннюю функцию write_everything,
# которая принимает произвольное количество аргументов и записывает их в указанный файл.
# Важно использовать режим 'a' для добавления данных в файл.
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for item in data_set:
                f.write(f"{item}\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])



from random import choice


class MysticBall: # Класс MysticBall принимает неограниченное количество строк и хранит их в атрибуте words.

    def __init__(self, *words):
        self.words = words

    def __call__(self): # Метод __call__ позволяет создавать экземпляры класса, которые могут вызываться как функции

        return choice(self.words) # и будут возвращать случайное слово из списка


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Возможный вывод: Да
print(first_ball())  # Возможный вывод: Нет
print(first_ball())  # Возможный вывод: Наверное