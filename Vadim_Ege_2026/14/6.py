def A(x):
    k = ''
    while x > 0:
        k += str(x % 9)
        x //= 9
    return k[::-1]


for x in range(1000):
    c = 81 ** 20 - 9 ** x + 50
    t = A(c)
    if sum(map(int, list(t))) == 138:
        print(x)  # ничего не выводит
