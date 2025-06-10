l = [int(x) for x in open('17.txt')]
mx = max([x for x in l if str(x)[-1] == '1'])
mn = []
for x in range(len(l) - 3):
    ch = 0
    if l[x] % 2 == 0:
        ch += 1
    if l[x + 1] % 2 == 0:
        ch += 1
    if l[x + 2] % 2 == 0:
        ch += 1
    if l[x + 3] % 2 == 0:
        ch += 1
    if ch % 2 != 0:
        if l[x] < mx and l[x + 1] < mx and l[x + 2] < mx and l[x + 3] < mx:
            mn.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
print(len(mn), min(mn))