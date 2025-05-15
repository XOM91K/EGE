l = [int(x) for x in open('20.txt')]
sr = [d for d in l if len(str(abs(d))) == 4 and str(abs((d)))[-1] == '3']
mx_sum = []
ct = 0
for x in range(len(l) - 2):
    d = [l[x], l[x + 1], l[x + 2]]
    d = sorted(d)
    if d[-1] + d[-2] > len(sr) ** 2:
        ct = ct + 1
        mx_sum.append( l[x] + l[x + 1] + l[x + 2] )
print(ct, abs(max(mx_sum)))