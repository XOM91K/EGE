sm = 0
x = 0
a = -1
while a != 0:
    a = int(input())
    if a % 2 == 0 and a % 5 == 0 and a != 0:
        x += 1
    sm += a
print(sm)
print(x)
