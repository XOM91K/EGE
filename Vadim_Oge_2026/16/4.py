a = int(input())
n = 0
s = 0
while a != 0:
    if a % 3 == 0 and a % 2 != 0:
        n += 1
    s += 1
    a = int(input())
print(s)
print(n)


