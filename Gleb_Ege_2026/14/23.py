def v7(n):
    s = ''
    while n > 0:
        s += str(n % 7)
        n //= 7
    return s[::-1]
l = []
for x in range(1000000, 1, -1):
    a = 7 ** 500 + 7 ** 200 - 7 ** 50 - x
    a = v7(a)
    if sum(map(int, a)) > 1199:
        print(sum(map(int, a)))