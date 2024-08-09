from pprint import pprint

name = 'sample2.txt'
with open(name, encoding='utf-8') as file:
    for line in file:
        for char in line:
            #print(line, end='')
            #print(char, end='')
            print(char)
    print (file.tell())