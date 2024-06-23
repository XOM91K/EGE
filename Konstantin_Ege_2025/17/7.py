l = [int(x) for x in open('7.txt')]
mx52 = 0
mn52 = 10 ** 10
mx_pair = 0
ct = 0
for x in l:
    if x % 100 == 52:
        mx52 = max(mx52, x)
        mn52 = min(mn52, x)
rzn = mx52 - mn52
for x in range(len(l) - 1):
    if (l[x] >= rzn and l[x + 1] < rzn) or (l[x] < rzn and l[x + 1] >= rzn):
        mx_pair = max(mx_pair, l[x] + l[x + 1])
        ct += 1
print(ct, mx_pair)