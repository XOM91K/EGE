import collections
l = [int(x) for x in open('8.txt')]
ct = 0
su = 0
ct_tr = 0
g = []
for x in l:
    if x % 17 == 0:
        ct += 1
        su += x
sr = su / ct
for x in range(len(l) - 2):
    if sum(map(int, str(l[x]))) == sum(map(int, str(l[x + 2]))) and l[x + 1] < sr:
        g.append(sum(map(int, str(l[x + 1]))))
        ct_tr += 1
print(ct_tr)
print(collections.Counter(g))