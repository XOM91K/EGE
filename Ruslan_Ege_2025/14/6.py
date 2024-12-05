def f(n):
    s = ''
    while n>0:
        s = str(n%9) + s
        n//=9
    return s
for x in range(1, 1000):
    a = 81 ** 20 - 9 ** x + 50
    a = f(a)
    if sum(map(int, a)) == 138:
        print(x)