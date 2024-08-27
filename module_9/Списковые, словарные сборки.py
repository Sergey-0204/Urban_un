# def by_3(x):
#     return x * 3
#
# def is_odd(x):
#     return x % 2
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(by_3, filter(is_odd, my_numbers))
# print(list(result))




# my_number =[3, 1, 4, 1, 5, 9, 2, 6]
# result = [x * 3 for x in my_number] # Аналог map
# print(result)




# my_number =[3, 1, 4, 1, 5, 9, 2, 6]
# result = [x * 3 for x in my_number if x % 2]
# print(result)
#




# my_number =['A', 1, 4, "B", 5, 'C', 2, 6]
# result = [x if type(x) == str else x * 5 for x in my_number]
# print(result)


# my_numbers =[3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# result = [x * y for x in my_numbers for y in they_numbers]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
# print(result)




