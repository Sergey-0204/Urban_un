immutable_var =(100, 500, "stroka", True)
print("Immutable tuple:", immutable_var)
#immutable_var[0]= 400  #Ошибка  сообщает нам, что кортеж не поддерживает обращение по элементам
#print(immutable_var)
metable_list = [immutable_var[0],immutable_var[1], immutable_var[2],immutable_var[3]]
metable_list[0] = 200
metable_list[3] = not True
print("Mutable list:", metable_list)