while 1 > 0:
    number =int(input('Введите число: '))
    if number % 2 == 0:
        print('число чётное')
        continue
    else:
        print('Число нечетное')
    print('Меня не забыли' )
    break
print('Я за циклом')