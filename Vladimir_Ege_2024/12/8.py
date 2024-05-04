l = []
for n in range(4, 1000):
    s = '7' + '1' * n
    while '1111' in s or '7777' in s:
        if '1111' in s:
            s = s.replace('1111', '77', 1)
        else:
            s = s.replace('7777', '1', 1)
    l.append(s.count('7') * 7 + s.count('1'))
print(max(l))