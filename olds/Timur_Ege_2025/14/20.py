def v25(a):
    s = []
    while a > 0:
        s.append(a % 25)
        a //= 25
    return s[::-1]
d = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
d = v25(d)
print(d)
print(d.count(0))