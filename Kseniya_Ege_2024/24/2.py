s = open('2.txt').readline()
alf = 'ABCDEHIJMOPQRSTUVWXYZ'
for x in alf:
    s = s.replace(x, '@')
s = s.split('@')
mx = 0
for x in s:
    if x not in '':
        for y in '0123456789':
            d = x
            d = d.split(y)
            for z in range(1, len(d) - 1):
                mx = max(mx, len(d[z]))
print(mx)