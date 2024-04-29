f = [int(x) for x in open('6.txt')]
mx = -99999
c = 0
mn = 10 ** 10
for y in range(1, len(f) - 1):
    if len(str(abs(f[y]))) == 3 and str(f[y])[-1] == str(f[y])[0]:
        mx = max(mx, f[y])
for i in range(1, len(f) - 1):
    if (((len(str(abs(f[i]))) == 4) + (len(str(abs(f[i + 1]))) == 4)) == 1) and (f[i] ** 2 + f[i + 1] ** 2) % mx == 0:
        c += 1
        mn = min(mn, f[i] + f[i + 1])
print(c, mn)
