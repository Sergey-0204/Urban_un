import area
def draw_area():
    for i in area:
        print(*i)
    print()

area = [["*", "*", "*",], ["*", "*", "*",], ["*", "*", "*"]]
print('Крестики-нолики')
print('______________________')
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char ='X'
        print('Ходят крестики')
    row = int(input("Введите номер строки 1,2,3 ")) -1
    column = int(input("Введите номер столбца 1,2,3 ")) -1
    if area[row][column] =="*":
        area[row][column] = turn_char
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        draw_area()
        continue
draw_area()
area[0][0] =='X' and area[0][1] =='X' and area[0][2] # проверка


draw_area()