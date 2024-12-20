l = [int(x) for x in open('4.txt')]
mx = min([d for d in l if str(d)[-2:] == '25'])
mx_sum = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4: # -965
        k = k + 1
    if len(str(abs(l[x+1]))) == 4:
        k = k + 1
    if len(str(abs(l[x+2]))) == 4:
        k = k + 1
    if k >= 2:
        if l[x] * l[x+1] * l[x+2] <= mx ** 2:
            ct = ct + 1
            mx_sum.append(l[x] * l[x+1] * l[x+2])
print(ct, max(mx_sum))