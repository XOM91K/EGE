import collections
l = [int(x) for x in open('4.txt')]
sr = [x for x in l if x % 17 == 0]
sr = sum(sr) / len(sr)
ct = 0
rr = []
for x in range(len(l) - 2):
    if sum(map(int, str(l[x]))) == sum(map(int, str(l[x + 2]))):
        if l[x + 1] < sr:
            rr.append(sum(map(int, str(l[x + 1]))))
            ct += 1
print(ct)
print(collections.Counter(rr))