def get_matrix(n, m, value):
    matrix = []  # Создаем пустой список для матрицы
    for i in range(n):  # цикл для создания строк матрицы, n повторов.
        in_matrix = []  # В первом цикле добавляем пустой список в список matrix.
        for j in range(m):  # Второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
            in_matrix.append(value)  # Во втором цикле пополняем ранее добавленный пустой список значениями value.
        matrix.append(in_matrix)  # Добавляем заполненную строку в матрицу
    return matrix

a = get_matrix(2, 2, 10)
b = get_matrix(3, 5, 42)
c = get_matrix(4, 2, 13)
print(a)
print(b)
print(c)
