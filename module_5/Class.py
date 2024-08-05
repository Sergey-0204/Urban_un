class Human:
    head = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут  {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения {self.age}')

    def __str__(self):
        return f'{self.name}'

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    def __bool__(self):
        return bool(self.age)

    def __del__(self):
        print(f'{self.name} ушел')


ser = Human('Ser', 22)
den = Human('Den', 45)
#if den:
    #den.say_info()
#print(den == ser)

# print(ser.name, ser.age)
# rint(den.name, den.age)
#del den
#ser.birthday()
#print(ser == den)
a = 6
print(ser)
print(Human.head)

