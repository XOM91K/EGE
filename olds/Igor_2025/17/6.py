l = [int(x) for x in open('6.txt')]
mx = max(l)
mn = min(l)
ct = 0
mx_pair = 0
for x in range(len(l) - 1):
    if l[x] % 3 == mx % 3 or l[x + 1] % 3 == mx % 3:
        if l[x] % 7 == mn % 7 or l[x + 1] % 7 == mn % 7:
            ct += 1
            mx_pair = max(mx_pair, l[x] + l[x + 1])
print(ct, mx_pair)