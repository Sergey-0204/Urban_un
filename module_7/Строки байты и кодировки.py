a ='hello' # ASCII
chars = []
for i in a:
   chars.append(ord(i))
print(chars)
s = " "
for i in chars:
    s += chr(i)
print(s)
