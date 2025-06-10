def v9(d):
    s = ""
    while d > 0:
        s += str(d % 9)
        d //= 9
    return s[::-1]
for x in range (1000):
    n= 81**20 - 9**x +50
    n = v9(n)
    if sum(map(int, n)) == 138:
        print(x)