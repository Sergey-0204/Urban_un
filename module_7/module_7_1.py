class Product:  # Класс Продукт
    def __init__(self, name, weight, category):  # принимает название, вес и категорию продукта
        self.name = name  # название продукта
        self.weight = weight  # общий вес товара
        self.category = category  # категория товара

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"  # возвращает строковое представление объекта


class Shop:  # Класс Магазин
    def __init__(self):
        self.__file_name = 'products.txt'  # инициализирует инкапсулированный атрибут __file_name с именем файла

    def get_products(
            self):  # читает содержимое файла и возвращает его как единую строку. Если файл не найден, возвращает пустую строку.
        try:
            with open(self.__file_name, 'r') as file:
                return ''.join(file.readlines())
        except FileNotFoundError:
            return ""

    def add(self, *products):  # принимает неограниченное количество объектов класса.
        existing_products = {line.split(',')[0] for line in self.get_products().strip().split('\n') if line}
        # Проверяем, есть ли продукт с таким же названием в файле. Если да, выводит сообщение о том, что продукт уже
        # есть. Если нет, добавляет продукт в файл.
        for product in products:
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')
                    file.close()

# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str

s1.add(p1, p2, p3)

print(s1.get_products())
