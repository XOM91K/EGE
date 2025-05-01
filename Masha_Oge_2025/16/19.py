a = -1
ct1 = 0
sm = 0
ct2 = 0
while a != 0:
    a = int(input())
    sm += a
    if a > 0:
        ct1 += 1
    if a < 0:
        ct2 += 1
print(sm)
print(ct1 - ct2)