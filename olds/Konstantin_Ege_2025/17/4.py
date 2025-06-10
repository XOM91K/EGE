l = [int(x) for x in open('4.txt')]
mx_pr_1 = 0
for x in range(len(l) - 1):
    if (str(l[x])[-1] == '1' and str(l[x + 1])[-1] != '1') or (str(l[x])[-1] != '1' and str(l[x + 1])[-1] == '1'):
        mx_pr_1 = max(mx_pr_1, l[x] + l[x + 1])
sr = mx_pr_1 / 2
ct = 0
mn = 10 ** 10
for x in range(len(l) - 1):
    if (str(l[x])[-1] == '1' and str(l[x + 1])[-1] != '1') or (str(l[x])[-1] != '1' and str(l[x + 1])[-1] == '1'):
        if l[x] < sr and l[x + 1] < sr:
            mn = min(mn, l[x], l[x + 1])
            ct += 1
mx = 0
for x in range(len(l) - 1):
    if (str(l[x])[-1] == '1' and str(l[x + 1])[-1] != '1') or (str(l[x])[-1] != '1' and str(l[x + 1])[-1] == '1'):
        if l[x] < sr and l[x + 1] < sr:
            if l[x] == mn or l[x + 1] == mn:
                print(l[x], l[x + 1])
                mx = max(mx, l[x], l[x + 1])
print(ct, mx)