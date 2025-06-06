def convert(n):
    s = ""
    while n > 0:
        s += str(n % 5)
        n = n // 5
    return s[::-1]

p = []
for x in range(1, 4000+1):
    t = 5 ** 17 + 5 ** 12 - x
    t1 = convert(t)
    p.append([t1.count("0"), x])
print(p)
print(max(p))