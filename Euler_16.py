a = (2**1000)
print(a)
print()
string_num = str(a)
mapObject = map(int, string_num)
digits = list(mapObject)
b = 0
for i in digits:
    b += i
print(b)