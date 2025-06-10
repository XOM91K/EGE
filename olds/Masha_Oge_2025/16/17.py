a = int(input())
sm = 0
for i in range(a):
    d = int(input())
    if d % 10 == 8:
        sm += d
print(sm)