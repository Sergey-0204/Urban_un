def generate_password():
    n = int(input("Введите число от 3 до 20: "))
    if n < 3 or n > 20:
        print("Число должно быть от 3 до 20")
        return

    pairs = []
    for i in range(1, 21):
        for j in range(1, 21):
            if i != j and (i + j) != n and n % (i + j) == 0:
                pairs.append((i, j))

    password = ''.join([str(pair[0]) + str(pair[1]) for pair in pairs])
    return password


# Пример использования
result = generate_password()
print(result)