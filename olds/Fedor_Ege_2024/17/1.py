l = [int(x) for x in open('1.txt')]
a = max([x for x in l if x % 19 == 0])
ct = 0
mx_pair = 0
for x in range(len(l) - 1):
    if l[x] > a or l[x + 1] > a:
        ct += 1
        mx_pair = max(mx_pair, l[x] + l[x + 1])
print(ct, mx_pair)