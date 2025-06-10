d = int(input())
sm = 0
for i in range(d):
    f = int(input())
    if f % 3 == 0 and f % 10 == 4:
        sm = sm + f
print(sm)