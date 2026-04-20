a = int(input())
sm = 0
pr = 1
ct1 = 0
ct2 = 0
while a != 0:
    if len(str(a)) == 2 and a % 6 == 0:
        ct1 += 1
        sm += a
    if len(str(a)) == 1 and a % 4 == 0:
        ct2 += 1
        pr *= a
    a = int(input())
if ct1 == 0:
    sm = -1
if ct2 == 0:
    pr = -1
print(sm, pr)