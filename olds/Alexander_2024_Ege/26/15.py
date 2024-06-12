l = [[int(d) for d in x.split()] for x in open('15.txt')]
l = sorted(l, key=lambda d: sum(d))
ct = 0
time_next = 0
print(l)
for x in l:
    if x[0] > time_next:
        time_next = sum(x)
        ct += 1
print(ct * 8)
mn = 10 ** 10
for x in l:
    if sum(x) >= 9829 + 233 and x[0] > 9768:
        mn = min(mn, x[0])
print(mn)