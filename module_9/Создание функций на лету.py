# my_func = lambda x: x + 10
#
# print(my_func(x=42))
# print(type(my_func))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map (lambda x: x + 10, my_numbers)
print (list(result))
