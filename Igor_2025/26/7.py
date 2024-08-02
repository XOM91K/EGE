l = [[int(d) for d in x.split()] for x in open('7.txt')]
l = sorted(l, key=lambda d: sum(d))
end_time = 0
pd = []
ct = 0
for y in l:
    if y[0] >= end_time:
        end_time = sum(y)
        pd.append(y)
        ct += 1
can = False
mx = 1384

for y in l:
    if y == [1384, 17]:
        can = True
    if can:
        mx = max(mx, y[0])
print(pd)
print(ct, mx - sum(pd[-2]))