def dev(d):
    s = ''
    while d > 0:
        s += str(d%9)
        d //= 9
    return s[::-1]
mx = 0
mx_pair = 0
ct = 0
l = [int(x) for x in open('16.txt')]
for x in l:
    if dev(abs(x))[-1] == '3':
        mx = max(mx,x)
#print(mx, dev(mx))
for x in range(len(l)-2):
    k = 0
    if len(str(abs(l[x]))) == 4 and abs(l[x]) % 2 == 0:
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and abs(l[x + 1]) % 2 == 0:
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and abs(l[x + 2]) % 2 == 0:
        k += 1
    if k <= 1 and (l[x] + l[x + 1] + l[x + 2]) <= mx:
        ct += 1
        mx_pair = max(mx_pair, l[x] + l[x + 1] + l[x + 2])
print(ct, mx_pair)