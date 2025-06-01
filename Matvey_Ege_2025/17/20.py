l = [int(x) for x in open('20.txt')]
mx25 = max([x for x in l if len(str(abs(x))) == 5 and str(x)[-2:] == '25']) ** 2
mn = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and str(l[x])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1])[-2:] == '25':
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2])[-2:] == '25':
        k += 1
    if k > 0:
        if l[x] ** 2 + l[x + 1] **2  + l[x + 2] ** 2 <= mx25:
            mn.append(l[x] ** 2 + l[x + 1] **2  + l[x + 2] ** 2)
print(len(mn), max(mn))