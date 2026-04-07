a = int(input())
d = 0
n = 0
while a != 0:
    n += 1
    if a % 3 == 0 and a % 2 != 0:
        d += 1
    a = int(input())
print(n)
print(d)