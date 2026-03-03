def F(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 2 == 0:
        return 11 * n + F(n - 1)
    else:
        return 11 * F(n - 2) + n
sm = 0
for n in range(35, 51):
    if F(n) % 2 == 0:
        sm += F(n)
print(len(str(sm)))