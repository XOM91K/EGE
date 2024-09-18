l = [int(x) for x in open('2.txt')]
ct = 0
mx = 0
ct_pairs = 0
mx_pair = 0
for x in l:
    ct_ch = 0
    ct_nch = 0
    for y in str(x):
        if int(y) % 2 == 0:
            ct_ch += 1
        else:
            ct_nch += 1
    if ct_ch == ct_nch:
        mx = max(mx, x)
for x in range(len(l) - 1):
    c = True
    for y in str(l[x]):
        for z in str(l[x + 1]):
            if y <= z:
                c = False
    if c and l[x] + l[x + 1] <= mx:
        ct_pairs += 1
        mx_pair = max(mx, l[x] + l[x + 1])
print(ct_pairs, mx_pair)