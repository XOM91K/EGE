l = [[int(d) for d in x.split()] for x in open('9.txt')]
for x in l:
    print(x)
print('--')
l = sorted(l, key=lambda d: d[1])
print(l)

ct_lec = 0
time_end = 0
pr = []
for x in l:
    if x[0] >= time_end:
        ct_lec += 1
        time_end = x[1]

        if ct_lec % 3 == 0:
            time_end += 10
        pr.append(x)
        print(x)
print(ct_lec)
print(pr)
l = sorted(l, key=lambda d: d[0])
print(l)