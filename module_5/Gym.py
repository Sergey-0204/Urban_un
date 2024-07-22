class GymProgram:
    def __init__(self, name):
        self.name = name
        self.program = []

    def add_exercise(self, exercise, sets, reps):
        self.program.append((exercise, sets, reps))

    def print_program(self):
        print(f"Программа тренировок для {self.name}:")
        for exercise, sets, reps in self.program:
            print(f"{exercise}: {sets} подходов по {reps} повторений")

# Создание программы тренировок
program = GymProgram("Начинающий")

# Добавление упражнений
program.add_exercise("Жим гантелей на наклонной скамье", 3, 12)
program.add_exercise("Приседания со штангой", 4, 10)
program.add_exercise("Тяга верхнего блока", 3, 15)
program.add_exercise("Отжимания", 3, 10)

# Вывод программы тренировок
program.print_program()