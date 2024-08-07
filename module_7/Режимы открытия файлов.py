from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r')  # r, w, a (read, write, append)
#file.read('\nprivet lol 2')
print(file.tell())
pprint(file.read())
print(file.seek(2))
pprint(file.read())
file.close()
