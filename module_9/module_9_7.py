def is_prime(func):
    # Это декоратор, который принимает функцию func в качестве аргумента. Внутри него определена функция wrapper,
    # которая вызывает func, получает результат и проверяет, является ли он простым числом.
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if result < 2:      # Проверка на простоту: Если результат меньше 2, он считается составным. Для других чисел
            # проверяется делимость на числа от 2 до квадратного корня из результата.
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")

        return result

    return wrapper


@is_prime # Функция, которая складывает три числа. Она декорирована с помощью @is_prime,
# что означает, что при вызове sum_three сначала будет выполнен декоратор.
def sum_three(a, b, c):
    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)