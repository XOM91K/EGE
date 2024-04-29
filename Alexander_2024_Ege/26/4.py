l = [[int(d) for d in x.split()] for x in open('4.txt')]
l = sorted([[r[1], r[0]] for r in l])
ct = 0
long_per = 0
tm = 0
last_mer = []
for x in l:
    if x[1] > tm and abs(tm - x[1]) >= 15:
        tm = x[0]
        ct += 1
        last_mer.append(x)
print(ct)
print(last_mer)
lm = last_mer[-2]
for x in l:
    if x[1] > lm[0]:
        long_per = max(long_per, abs(x[0] - lm[0]))
print(long_per)