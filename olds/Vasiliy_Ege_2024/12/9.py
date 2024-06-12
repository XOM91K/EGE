r = []
for x in range(4, 2000):
    s = '5' + '5' * x
    while '25' in s or '355' in s or '5555' in s:
        if '25' in s:
            s = s.replace('25', '33', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '5555' in s:
            s = s.replace('5555', '2', 1)
    r.append(s.count('2'))
print(max(r))