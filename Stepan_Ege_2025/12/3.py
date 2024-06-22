ct = 0
s = '5' * 400
while '555' in s or '333' in s:
    if '555' in s:
        s = s.replace('555', '3', 1)
    else:
        s = s.replace('333', '5', 1)
        ct += 3
print(ct)