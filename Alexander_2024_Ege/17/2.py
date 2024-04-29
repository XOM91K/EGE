l = [int(x) for x in open('2.txt')]
mx_25 = max([x for x in l if str(x)[-2:] == '25'])
ct = 0
mx = 0
for x in range(len(l) - 2):
    d = [l[x], l[x + 1], l[x + 2]]
    ct_4 = len([y for y in d if len(str(abs(y))) == 4])
    if ct_4 <= 2 and sum(d) <= mx_25:
        ct += 1
        mx = max(mx, sum(d))
print(ct, mx)
