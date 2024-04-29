a = 1
sm = 0
pr = 1
ct = 0
while a >= 0:
    a = int(input())
    if a % 5 == 0:
        sm += a
    if a % 10 == 3:
        pr *= a
    if a > 150:
        ct += 1
print(sm, pr, ct)