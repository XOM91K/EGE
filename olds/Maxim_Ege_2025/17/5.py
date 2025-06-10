l = [int(x) for x in open('5.txt')]
ct = 0
posl = []
a = []
for x in range(len(l)):
    if str(l[x])[-1] == '7':
        a.append(l[x])
b = max(a)
for x in range(len(l) - 2):
    if (l[x] % 2 != 0 and l[x+1] % 2 != 0 and l[x+2] % 2 == 0) or (l[x] % 2 == 0 and l[x+1] % 2 != 0 and l[x+2] % 2 != 0) or (l[x] % 2 != 0 and l[x+1] % 2 == 0 and l[x+2] % 2 != 0):
        if (l[x] > b and l[x+1] <= b and l[x+2] <= b) or (l[x] <= b and l[x+1] <= b and l[x+2] > b) or (l[x] <= b and l[x+1] > b and l[x+2] <= b):
            ct += 1
            posl.append(l[x])
            posl.append(l[x + 1])
            posl.append(l[x + 2])
f = set(posl)
d = sum(f)/len(f)
print(ct, str(d)[:3])