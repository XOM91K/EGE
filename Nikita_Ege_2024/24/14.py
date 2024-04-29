s = open('14.txt').readline()
d = 'AEIOUY'
for x in d:
    s = s.replace(x, '@')
s = s.split('@')
ct = 0
for x in s:
    if len(x) >= 7:
        for y in range(len(x) - 6):
            if x[y] + x[y + 1] + x[y + 2] == (x[y + 4] + x[y + 5] + x[y + 6])[::-1]:
                ct += 1
print(ct)