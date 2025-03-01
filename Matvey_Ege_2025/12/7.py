r = []
for n in range(4, 10000):
    s = '7' + '6' * n
    while '766' in s or '667' in s:
        if '766' in s:
            s = s.replace('766', '67', 1)
        if '667' in s:
            s = s.replace('667', '7', 1)

    r.append(s)
print(len(set(r)))