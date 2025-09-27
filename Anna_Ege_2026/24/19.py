import collections
s = open(r'C:\Users\Zarif\Downloads\24_887.txt').readline()
alf = ''
for x in range(len(s) - 1):
    if s[x] == 'X':
        alf += s[x + 1]
print(collections.Counter(alf))