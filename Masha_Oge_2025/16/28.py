a = -1
sm = 0
pr = 1
while a != 0:
    a = int(input())
    if 1 <= a // 10 <= 9 and a % 6 == 0:
        sm += a
    if a // 10 < 1 and a % 4 == 0 and a != 0:
        pr *= a
if sm == 0:
    sm = -1
if pr == 1:
    pr = -1
print(sm, pr)