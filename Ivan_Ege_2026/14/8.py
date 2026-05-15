# def v5(d):
#     s = ''
#     while d > 0:
#         s = str(d % 5) + s
#         d //= 5
#     return s
# for x in range(1, 4001):
#     d = 5 ** 17 + 5 ** 12 - x
#     d = v5(d)
#     if d.count('0') > 9:
#         print(x)
#

def f(n):
    c = 0
    while n > 0:
        if n % 5 == 0:
            c += 1
        n //= 5
    return c

mx = []
for x in range(1, 4001):
    a = 5 ** 17 + 5 ** 12
    a -= x
    mx.append([x, f(a)])
print(sorted(mx, key=lambda x: (-x[1], x[0])))