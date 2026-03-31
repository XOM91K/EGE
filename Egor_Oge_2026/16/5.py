a = int(input())
sm = 0
while a != 0:
    if len(str(a)) == 2 and a % 8 == 0:
        sm += a
    a = int(input())
print(sm)
