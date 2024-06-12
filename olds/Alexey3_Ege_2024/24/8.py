import collections, itertools
s = open('8.txt').readline()
mx = collections.Counter(s)
#DVE
#FNI
ct = 0
for i in 'DVE':
    for j in 'FNI':
        ct += s.count(i + j)
        ct += s.count(j + i)
print(ct)