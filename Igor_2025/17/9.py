l = [int(x) for x in open('9.txt')]
mn = min(l) % 5
mx = max(l) % 7
mx_sm = 0
ct = 0
for x in range(len(l) - 2):
    if len(str(l[x])) == 4 or len(str(l[x + 1])) == 4 or len(str(l[x + 2])) == 4:
        v2 = [int((d % 5) == mn) for d in [l[x], l[x + 1], l[x + 2]]]
        v3 = [int((d % 7) == mx) for d in [l[x], l[x + 1], l[x + 2]]]
        if sum(v2) <= 1 and sum(v3) >= 2:
            mx_sm = max(mx_sm, sum([l[x], l[x + 1], l[x + 2]]))
            ct += 1
print(ct, mx_sm)