sm = 0
a = -1
while a != 0:
    a = int(input())
    if len(str(a)) == 2 and a % 8 == 0:
        sm += a
print(sm)