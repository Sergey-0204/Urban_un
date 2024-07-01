def generate_primes(n):
    primes = []  # Список для хранения пар

    for i in range(1, 20):  # Цикл для выбора первого числа пары
        for j in range(i + 1, 21):  # Цикл для выбора второго числа пары
            if (i + j) % n == 0:  # Проверка кратности суммы числа n
                primes.append(f"{i}{j}")

    result = ''.join(primes)  # Объединяем все пары в одну строку
    return result


print(generate_primes(9))
