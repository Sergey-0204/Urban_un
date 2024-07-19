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


   def __len__(self):
       return self.age

  def __del__(self):
      print(f'{self.name} ушел')



ser = Human('Ser', 22)
den = Human('Den', 45)
#print(ser.name, ser.age)
#rint(den.name, den.age)
del den
ser.birthday()
print(len(ser))
