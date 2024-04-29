import re
s = open(r'C:\Users\Zarif\Downloads\24_617_1.txt').readline()
sl = {}
for x in range(len(s) - 1):
    if s[x] == 'E':
        if s[x + 1] not in sl:
            sl[s[x + 1]] = 0
        sl[s[x + 1]] += 1
print(sl)