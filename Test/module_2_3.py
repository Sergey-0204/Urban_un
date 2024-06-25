my_list = [42, 69, 322, 0, 13, 99, -5, 9, 8, 7, -6, 5]
index = 0

while index < len(my_list):

    if my_list[index] > 0:
        print(my_list[index])
    elif my_list[index] == 0:
        var = 1
    else:
        break
    index += 1

