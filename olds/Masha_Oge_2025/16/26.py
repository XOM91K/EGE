a = int(input())
sm = 0
for i in range(a):
    b = int(input())
    if b % 6 == 0:
        sm += b
print(sm)