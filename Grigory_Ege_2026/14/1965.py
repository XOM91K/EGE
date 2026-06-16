A = []
def v38(d):
    s = []
    while d > 0 :
        s.append(d%38)
        d //= 38
    return s[::-1]
for x in range(0,20_001):
    n = v38(x**2 + 17*x + 53)
    kl10 = [y for y in n if y == 10]
    if len(kl10) > 2:
        A.append(x)
        print(x, len(kl10))
print(max(A))
print(10024**2+17*10024+53)