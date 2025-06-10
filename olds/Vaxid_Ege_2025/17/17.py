l = [int(x) for x in open('17.txt')]
mn = min([d for d in l if str(d)[-1] == '6' and len(str(d)) == 4 and d > 0])
mx_sum = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and str(l[x])[-1] == '6':
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and str(l[x + 1])[-1] == '6':
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and str(l[x + 2])[-1] == '6':
        k += 1
    if k == 1:
        if l[x] + l[x + 1] + l[x + 2] <= mn:
            ct += 1
            mx_sum.append(l[x] + l[x + 1] + l[x + 2])
print(ct, max(mx_sum))