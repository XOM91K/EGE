mx = 0
for n in range(4, 10000 + 1):
    s = '3' + n * '5'
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    mx = max(mx, s.count('5') * 5 + s.count('3') * 3)
print(mx)