def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1

obj = func_generator(10)
print(obj)

for i in obj:
    print(i)
