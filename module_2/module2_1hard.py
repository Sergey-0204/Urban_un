def generate_primes(n):
    n = int(input("Введите число от 3 до 20: "))

    if n < 3 or n > 20:
        print("Число должно быть от 3 до 20")
        return

    primes = []  # Список для хранения пар

    for i in range(1, 20):  # Цикл для выбора первого числа пары
        for j in range(i + 1, 21):  # Цикл для выбора второго числа пары
            if n % (i + j) == 0 and i + j <= n:  # Проверка кратности суммы числа n
                primes.append(f"{i}{j}")

    result = ''.join(primes)  # Объединяем все пары в одну строку
    return result


print(generate_primes(n=0))


