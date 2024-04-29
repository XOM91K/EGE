l = [[int(d) for d in x.split()] for x in open('5.txt')]
print(l)
mx_sm = 0
ct_nch = 0
mn_rzn = 10 ** 10
for x in l:
    if max(x) % 2 != 0:
        ct_nch += 1
    if max(x) % 2 != 0 and min(x) % 2 == 0:
        mn_rzn = min(mn_rzn, max(x) - min(x))
    mx_sm += max(x)
if ct_nch % 2 != 0:
    print(mx_sm - mn_rzn)
else:
    print(mx_sm)