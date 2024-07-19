class Human:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.say_info()
  def say_info(self):
      print(f'Привет, меня зовут  {self.name}, мне {self.age}')

  def birthday(self):
      self.age += 1
      print(f'У меня день рождения {self.age}')



ser = Human('Ser', 22)
den = Human('Den', 45)
#print(ser.name, ser.age)
#rint(den.name, den.age)
ser.birthday()