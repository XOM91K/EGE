qwerty = 0
for i in range(10000, 100000):
    x = oct(i)[2:]
    x = x.replace('1', '2')
    x = x.replace('3', '2')
    x = x.replace('5', '2')
    x = x.replace('7', '2')
    x += str(i % 8)
    x = int(x, 8)
    y = x
    x = oct(y)[2:]
    x = x.replace('1', '2')
    x = x.replace('3', '2')
    x = x.replace('5', '2')
    x = x.replace('7', '2')
    x += str(y % 8)
    x = int(x, 8)
    if x % 2023 == 0:
        qwerty += i
print(qwerty)