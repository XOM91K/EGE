l = [int(x) for x in open('8.txt')]
mx = max(l)
mn = min(l)
mx_sm = []
for x in range(len(l) - 1):
    if l[x] % 3 == mx % 3 or l[x + 1] % 3 == mx % 3:
        if l[x] % 7 == mn % 7 or l[x + 1] % 7 == mn % 7:
            mx_sm.append(l[x] + l[x + 1])
print(len(mx_sm), max(mx_sm))