#************
l = [int(x) for x in open('16.txt')]
sk =[d for d in l if str(d)[-1] == '3' and len(str(abs(d))) == 4]
mx_sum = []
ct = 0
for x in range(len(l) - 2):
    r = sorted([l[x], l[x + 1], l[x + 2]])
    if r[-2] + r[-1] > len(sk) ** 2:
        ct = ct + 1
        mx_sum.append( abs(l[x] + l[x + 1] + l[x + 2]) )
print(ct, max(mx_sum))