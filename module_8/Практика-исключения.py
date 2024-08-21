def calc(line):
    operand_1, operantion, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operantion == '+':
        print(f'Результат:{operand_1 + operand_2}')
    if operantion == '-':
        print(f'Результат:{operand_1 - operand_2}')
    if operantion == '/':
        print(f'Результат:{operand_1 / operand_2}')
    if operantion == '//':
        print(f'Результат:{operand_1 // operand_2}')
    if operantion == '%':
        print(f'Результат:{operand_1 % operand_2}')
    if operantion == '*':
        print(f'Результат:{operand_1 * operand_2}')
cnt = 0


with open('data.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            print(f'Ошибка в линии {cnt}, возникло {exc} с параметрами {exc.args}')
