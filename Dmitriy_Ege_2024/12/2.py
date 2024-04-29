mx = 0
for x in range(301, 500):
    s1 = '5' * x
    while '55555' in s1:
        s1 = s1.replace('55555', '88', 1)
        s1 = s1.replace('888', '55', 1)
    print(x, s1.count('5'))
    mx = max(mx, s1.count('5'))