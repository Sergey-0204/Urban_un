class Vehicle:   # Класс Vehicle
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black',
                        'white']  # Атрибут класса __COLOR_VARIANTS хранит допустимые цвета

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color # Содержит атрибуты owner, __model, __engine_power, __color

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"  # Методы get_model(), get_horsepower(), get_color() возвращают  соответствующие строки с информацией

    def print_info(self): # выводит информацию о модели, мощности, цвете и владельце.
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}") #  проверяет, можно ли изменить цвет на новый. Если новый цвет допустим, меняет его
            # если нет — выводит сообщение об ошибке.


class Sedan(Vehicle): # Класс Sedan, наследуется от класса Vehicle
    __PASSENGERS_LIMIT = 5 # Содержит атрибут класса, который равен 5

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)
#  Конструктор вызывает конструктор родительского класса для инициализации общих атрибутов

# Пример использования классов
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')  # Нельзя сменить цвет на Pink
vehicle1.set_color('BLACK')  # Успешно меняем цвет на BLACK
vehicle1.owner = 'Vasyok'  # Меняем владельца

# Проверяем что поменялось
vehicle1.print_info()
