class StepValueError(ValueError):   # класс ошибки StepValueError, который будет использоваться, когда шаг равен нулю.
    pass


class Iterator: # создаем собственный класс Iterator
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

        self.start = start  # начальное значение итерации.
        self.stop = stop  # конечное значение итерации.
        self.step = step  # шаг итерации (по умолчанию равен 1).
        self.pointer = start # текущее значение итерации, инициализируется значением start.

    def __iter__(self):  # Этот метод возвращает сам объект итератора и сбрасывает указатель на начальное значение
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration    # Если шаг положительный (self.step > 0), итерация продолжается,
            # пока указатель больше конечного значения (self.stop).
            # Если шаг отрицательный (self.step < 0), итерация продолжается, пока указатель меньше конечного значения.

        current_value = self.pointer  # Сохраняем текущее значение указателя в переменной
        self.pointer += self.step  # Увеличиваем  указатель на величину шага.
        return current_value # Возвращаем текущее значение.


# Пример выполняемого кода
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()