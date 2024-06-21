a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))


a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))

a = [1, 2.2, 'python']
print(type(a))
a = [5,10,15,20,25,30,35,40]
print("a[2] =", a[2])

print("a[0:3] =", a[0:3])

print("a[5:] =", a[5:])

a = [1,2,3]
a[2] = 4
print(a)