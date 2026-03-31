l = [[int(d) for d in x.split()] for x in open('24.txt')]
minutes = [0] * 44640
for x in range(len(minutes)):
    for y in l:
        if y[0] <= x < y[1]:
            minutes[x] = '1'
ct_m = 0
for x in minutes:
    if x == '1':
        ct_m += 1
print(ct_m)