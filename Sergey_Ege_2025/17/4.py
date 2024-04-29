l = [int(x) for x in open('4.txt')]
mx_pair = 0
for x in range(len(l) - 1):
    k = 0
    if len(str(l[x])) == 2:
        k += 1
    if len(str(l[x + 1])) == 2:
        k += 1
    if k == 1:
        mx_pair = max(mx_pair, l[x] + l[x + 1])
print(mx_pair)
ct = 0
mn = 10 ** 10
for x in l:
    if x > mx_pair:
        ct += 1
        mn = min(mn, x)
print(ct, mn)