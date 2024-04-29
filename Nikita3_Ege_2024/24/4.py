import collections
s = open('4.txt').readline()
s2 = ''
for x in range(len(s) - 2):
    if s[x] == 'X' and s[x + 2] == 'Z':
        s2 += s[x + 1]
print(collections.Counter(s2))