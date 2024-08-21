# def greet_person(person_name):
#     if person_name == 'ВоланДеМорт':
#         raise Exception ("Мы не любим тебя, ВаланДеМорт")
#     print(f'Привет, {person_name}')
#
# greet_person("Дорогой ученик")
# greet_person('ВоланДеМорт')

# try:
#     raise NameError('Привет Там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} Пролетело мимо! его параметр {exc.args}')
#     raise



class ProZero(Exception):
    pass
def f(a, b):
    if b == 0:
        raise ProZero ('Деление на ноль невозможно')
    return a / b

