a = 1
sm = 0
while a != 0:
    a = int(input())
    if 100 <= a <= 999 and a % 4 == 0:
        sm += a
print(sm)