import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.color = [222, 35, 130]  # Изначальный цвет

    def set_color(self, r, g, b):
        if all(0 <= value <= 255 for value in (r, g, b)):
            self.color = [r, g, b]

    def get_color(self):
        return self.color

    def set_sides(self, sides):
        # Круг не имеет сторон в традиционном понимании, но мы можем задать количество точек для представления
        if isinstance(sides, int) and sides > 0:
            self.sides = sides

    def get_sides(self):
        return [self.radius] * self.sides if hasattr(self, 'sides') else [self.radius]

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __len__(self):
        return self.perimeter()


class Cube:
    def __init__(self, side_length):
        self.side_length = side_length
        self.color = [255, 255, 255]  # Изначальный цвет (белый)

    def set_color(self, r, g, b):
        if all(0 <= value <= 255 for value in (r, g, b)):
            self.color = [r, g, b]

    def get_color(self):
        return self.color

    def set_sides(self, *sides):
        if len(sides) == 6 and all(side > 0 for side in sides):
            self.sides = sides

    def get_sides(self):
        return getattr(self, 'sides', (self.side_length,) * 6)

    def get_volume(self):
        return self.side_length ** 3


# Пример использования классов
circle1 = Circle(radius=15)
cube1 = Cube(side_length=6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [255, 255, 255]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # (6, 6, 6, 6, 6, 6)
circle1.set_sides(15)  # Изменится (по сути это не влияет на круг)
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Длина окружности (периметр)

# Проверка объёма (куба):
print(cube1.get_volume())  # Объем куба

