s = open('1.txt').readline()
for x in 'VXZ':
    s = s.replace(x, '#')
s = s.split('#')
mx = 0
for x in s:
    can = True
    for y in 'AEIOUY':
        if x.count(y) > 8:
            can = False
            break
    if can:
        mx = max(mx, len(x))
print(mx)