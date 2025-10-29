def v7(n):
    s = ''
    while n > 0:
        s += str(n%7)
        n //= 7
    return s [::-1]
for x in range(1 , 2031):
    n = 7 ** 170 + 7 ** 100 - x
    n = v7(n)
    if n.count('0') > 72:
        print(n.count('0'), x)