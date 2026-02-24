import collections
s = open('43.txt').readlines()
for x in s:
    x = x.strip()
    if x.count('Q') == 64:
        print(collections.Counter(x))
s = open('43.txt').read().count('C')
print(s)