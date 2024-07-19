class Human:
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def say_info(self):
      print(f'Привет, меня зовут  {self.name}, мне {self.age}')



ser = Human('Ser', 22)
den = Human('Den', 45)
#print(ser.name, ser.age)
#rint(den.name, den.age)
ser.say_info()