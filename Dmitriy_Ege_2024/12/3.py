l = []
for x in range(2, 500):
    s = '8' * x
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    l.append(s)
print(set(l))