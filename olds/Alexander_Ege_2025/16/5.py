# https://examinf.ru/tasks/762
def F(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return F(n - 1) + 2 * n - 1
    if n % 2 == 0:
        return 4 * F(n / 2)
for a in range(0, 1000):
    for b in range(0, 1000):
        if F(a) - F(b) == 1045:
            # 10 - 40 = -30
            print(abs(a - b), a, b)