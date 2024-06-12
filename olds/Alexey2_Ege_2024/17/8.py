def v6(n):
    s = ''
    while n > 0:
        s += str(n % 6)
        n //= 6
    return s[::-1]
l = [int(x) for x in open('8.txt')]
mx = 0
ct = 0
mx_tr = 0
for x in l:
    if v6(x)[-2:] == '23':
        mx = max(mx, x)
for x in range(len(l) - 2):
    r = [l[x], l[x + 1], l[x + 2]]
    ln = [len(str(abs(l[x]))), len(str(abs(l[x + 1]))), len(str(abs(l[x + 2])))]
    if ln.count(4) == 1:
        if sum(r) % mx == 0:
            ct += 1
            mx_tr = max(mx_tr, sum(r))
print(ct, mx_tr)