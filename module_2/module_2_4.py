numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == numbers[0]:
        numbers.remove(i)
# print(numbers)
for num in numbers:
    is_prime = True
    if num < 2:
        is_prime =False
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print('Простые числа: ',primes)
print('Непростые числа: ', not_primes)
