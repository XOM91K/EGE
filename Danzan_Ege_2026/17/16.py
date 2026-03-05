def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d//x)
    return sorted(set(l))
mn = []
l = [int(x) for x in open('16.txt')]
for x in range(len(l) - 1):
    #if dels(l[x]) != dels(l[x + 1]):
    if l[x] % 2 != l[x + 1] % 2:
        if len(set(dels(l[x])) & set(dels(l[x + 1]))) == 0:
            mn.append(l[x] + l[x + 1])
print(len(mn), min(mn))