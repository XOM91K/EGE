l = [int(x) for x in open("30.txt")]
mn = min([x for x in l if len(str(abs(x))) == 4 and sum(map(int, str(abs(x)))) == 21 and x > 0])
print(mn)
ct = 0
mx = 0
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and sum(map(int, str(abs(l[x])))) == 15:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and sum(map(int, str(abs(l[x + 1])))) == 15:
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and sum(map(int, str(abs(l[x + 2])))) == 15:
        k += 1
    if k == 2:
        print(l[x], l[x + 1], l[x + 2])
        if 98 * (l[x] + l[x + 1] + l[x + 2]) >= mn ** 2:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct, mx)