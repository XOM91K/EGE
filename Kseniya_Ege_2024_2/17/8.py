l = [int(x) for x in open('8.txt')]
mx = 0
ct = 0
mn = 10 ** 10
for x in l:
    if str(abs(x))[0] == '8':
        mx = max(mx, x)
for x in range(len(l) - 2):
    ll = [str(abs(l[x]))[0], str(abs(l[x + 1]))[0], str(abs(l[x + 2]))[0]]
    if ll.count('6') <= 1:
        if l[x] + l[x + 1] + l[x + 2] >= mx:
            ct += 1
            mn = min(mn, l[x] + l[x + 1] + l[x + 2])
print(ct, mn)