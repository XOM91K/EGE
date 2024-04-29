s = open(r'22.txt').readline()
s = s.replace('N', 'K')
s = s.replace('L', 'K')
s = s.replace('F', 'K')
mx = 0
for x in '02468':
    f = s.split(x)
    for y in f[1:-1]:
        if y.count('K') == len(y):
            mx = max(mx, len(y))
print(mx)