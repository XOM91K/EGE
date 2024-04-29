s = open(r'C:\Users\Zarif\Downloads\24 (10).txt').readline()
import string
for x in 'AEIOUY':
    s = s.replace(x, '#')
for x in 'BCDFGHJKLMNPQRSTVWXZ':
    s = s.replace(x, '@')
print(s)
mx = 0
ct = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx)