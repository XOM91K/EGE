l = [int(x) for x in open('17.txt')]
mn6 = min([d for d in l if len(str(abs(d))) == 4 and str(abs(d))[-1] == '6' and d > 0])
print(mn6)
mx = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 4 and str(l[x])[-1] == '6':
        k += 1
    if len(str(abs(l[x + 1]))) == 4 and str(l[x + 1])[-1] == '6':
        k += 1
    if len(str(abs(l[x + 2]))) == 4 and str(l[x + 2])[-1] == '6':
        k += 1
    if k == 1:
        if l[x] + l[x + 1] + l[x + 2] <= mn6:
            mx.append(l[x] + l[x + 1] + l[x + 2])
print(len(mx), max(mx))