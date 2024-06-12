mx = []
for n in range(4, 10000):
    s = '8' + n * '4'
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    mx.append(s.count('4') * 4 + s.count('8') * 8 + s.count('1'))
print(max(mx))