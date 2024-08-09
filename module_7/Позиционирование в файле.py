import io
from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r', encoding='utf-8')  # r, w, a (read, write, append)
#file.read('\nprivet lol 2')
print(file.writable())
print(file.readable())
print(file.seekable())
print(file.closed)
print(file.tell())
pprint(file.read())
#file.seek(15)
#file.write(' new text')
print(file.tell())
print(file.name)
print(file.buffer)
file.close()
