class User:
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
    def __init__(self):
        print('Я в ините')

user1 = User()
print(User.__mro__)
