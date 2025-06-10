l = [int(x) for x in open('10.txt')]
mn4 = 10 ** 10
mx4 = 0
ct = 0
mx = 0
for x in l:
    if x % 10 == 4:
        mn4 = min(mn4, x)
        mx4 = max(mx4, x)
sm = mn4 + mx4
for x in range(len(l) - 1):
    if l[x] + l[x + 1] < sm:
        ct += 1
        mx = max(mx, l[x] + l[x + 1])
print(ct, mx)