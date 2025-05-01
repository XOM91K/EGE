a = -1
sm = 0
while a != 0:
    a = int(input())
    if a // 10 == 0 and a % 3 == 0:
        sm += a
print(sm)