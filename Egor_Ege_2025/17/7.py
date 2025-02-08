def f(n, a):
    dels = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            dels.append(x)
            dels.append(n // x)
    dels_a = []
    for y in range(1, int(a ** 0.5) + 1):
        if a % y == 0:
            dels_a.append(y)
            dels_a.append(a // y)
    dels_a = sorted(dels_a)
    del dels_a[0]
    dels = sorted(dels)
    del dels[0]
    for i in dels:
        for j in dels_a:
            if i == j:
                return False
    return True

cnt = 0
d = []
l = [int(x) for x in open('7.txt')]
for x in range(len(l) - 1):
    if f(l[x], l[x+1]):
        if l[x] % 2 != l[x+1] % 2:
            cnt += 1
            d.append(sum([l[x], l[x+1]]))
            print([l[x], l[x+1]])
print(cnt, min(d))