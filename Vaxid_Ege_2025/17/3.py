l = [int(x) for x in open('3.txt')]
mx = max([d for d in l if str(d)[-2:] == '17'])
mx_sum = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if len(str(l[x])) == 4:
        k += 1
    if len(str(l[x + 1])) == 4:
        k += 1
    if len(str(l[x + 2])) == 4:
        k += 1
    if k == 2:
        if l[x] % 5 == 0 or l[x + 1] % 5 == 0 or l[x + 2] % 5 == 0:
            if l[x] + l[x + 1] + l[x + 2] > mx:
                ct += 1
                mx_sum.append(l[x] + l[x + 1] + l[x + 2])
print(ct, max(mx_sum))