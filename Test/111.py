def check_winner():
    for a in ['X','Y']:

        for i in range(3):
            if area[i][0] == area[i][1] == area[i][2] == a:
                return a

        for i in range(3):
            if area[0][i] == area[1][i] == area[2][i] == a:
                return a

        if area[0][0] == area[1][1] == area[2][2] == a:
            return a
        elif area[0][2] == area[1][1] == area[2][0] == a:
            return a
def draw_area():
    for i in area:
        print(*i)
    print()


area = [["*", "*", "*", ], ["*", "*", "*", ], ["*", "*", "*"]]
print('Крестики-нолики')
print('______________________')
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input("Введите номер строки 1,2,3 ")) - 1
    column = int(input("Введите номер столбца 1,2,3 ")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        draw_area()
        continue

    draw_area()

    if check_winner() == "X":
        print("Победа крестиков")
        break
    if check_winner() == "0":
        print("Победа ноликов")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья")