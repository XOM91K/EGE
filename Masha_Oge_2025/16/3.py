n = 1
sm = 0
while n != 0:
    n = int(input())
    if n % 8 == 0 and 1 <= n // 10 <= 9:
        sm += n
print(sm)