l = [int(x) for x in open('2.txt')]
ct_tre = 0
mx_tre = 0
mn_52 = min([x for x in l if x % 52 == 0])
for x in range(len(l) - 2):
    if (l[x] % 113 + l[x + 1] % 113 + l[x + 2] % 113) == mn_52:
        ct_tre += 1
        mx_tre = max(mx_tre, l[x] + l[x + 1] + l[x + 2])
print(ct_tre, mx_tre)