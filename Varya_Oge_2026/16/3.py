d = -1
sm = 0
while d != 0:
    d = int(input())
    if d % 8 == 0 and len(str(d)) == 2:
        sm = sm + d
print(sm)