a = int(input())
sm = 0
while a != 0:
    if a % 3 == 0 and len(str(a)) == 1:
        sm += a
    a = int(input())
print(sm)