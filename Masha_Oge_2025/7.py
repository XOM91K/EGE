a = int(input())
sm = 0
for x in range(a):
    num = int(input())
    if num % 3 == 0 and num % 10 == 4:
        sm += num
print(sm)