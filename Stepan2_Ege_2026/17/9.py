l = [int(x) for x in open('9.txt')]
mx5 = max([d for d in l if str(d)[-1] == '3' and len(str(abs(d))) == 5])
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and str(l[x])[-1] == '3':
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1])[-1] == '3':
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2])[-1] == '3':
        k += 1
    if k >= 2:
        if l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 <= mx5 ** 2:
            mn.append(l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2)
print(len(mn), min(mn))