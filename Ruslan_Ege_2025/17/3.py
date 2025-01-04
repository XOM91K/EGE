l = [int(x) for x in open('3.txt')]
mx3 = []
ct_pair = 0
mn_pair = []
for x in l:
    if str(x)[-1] == '3':
        mx3.append(x)
mx3 = max(mx3) ** 2
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and str(l[x])[-1] == '3':
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1])[-1] == '3':
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2])[-1] == '3':
        k += 1
    if k >= 2:
        if l[x] ** 2 + l[x +1 ] ** 2 + l[x + 2] ** 2 <= mx3:
            ct_pair += 1
            mn_pair.append(l[x] ** 2 + l[x + 2] ** 2 + l[x + 1] ** 2)
print(ct_pair, min(mn_pair), len(mn_pair))