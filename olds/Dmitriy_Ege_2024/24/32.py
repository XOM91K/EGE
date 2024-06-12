import collections
s = open('32.txt').readline()
ct = 0
for i in 'DVE':
    for j in 'INF':
        ct += s.count(i + j)
        ct += s.count(j + i)
print(ct)
print(collections.Counter(s))