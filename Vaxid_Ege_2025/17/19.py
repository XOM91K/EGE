l = [int(x) for x in open('19.txt')]
mn = min([d for d in l if len(str(abs(d))) == 4 and d % 17 == 0])
mn_sum = []
ct = 0
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and str(l[x])[-2:] == '27':
        k = k + 1
    if len(str(abs(l[x + 1]))) == 4 and str(l[x + 1])[-2:] == '27':
        k = k + 1
    if len(str(abs(l[x + 2]))) == 4 and str(l[x + 2])[-2:] == '27':
        k = k + 1
    if k >= 1:
        if ( l[x]** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 ) <= mn ** 2:
            ct = ct + 1
            mn_sum.append( abs(l[x]) + abs(l[x + 1]) + abs(l[x + 2]) )
print(ct, min(mn_sum))