import collections
s = open('6.txt').readline()
p = ''
for x in range(len(s) - 3):
    if s[x] == s[x + 1] == s[x + 2]:
        p += s[x + 3]
print(collections.Counter(p))