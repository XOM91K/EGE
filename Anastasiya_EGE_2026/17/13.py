l = [int(x) for x in open('13.txt')]
ch=min([x for x in l if x%2==0])
mn = []
for x in range(len(l)-2):
    k = 0
    if l[x] % 2 == 0:
        k += 1
    if l[x + 2] % 2 == 0:
        k += 1
    if k == 1:
        if l[x + 1] % ch == 0:
            mn.append(l[x] + l[x + 2])
print(len(mn), min(mn))