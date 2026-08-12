a = -1
sm = 0
mn = 1
while a != 0:
    a = int(input())
    if a != 0:
        if len(str(a)) == 2 and a % 6 == 0:
            sm += a
        if len(str(a)) == 1 and a % 4 == 0:
            mn *= a
if sm == 0:
    sm = -1
if mn == 1:
    mn = -1
print(sm, mn)