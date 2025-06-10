l = [int(x) for x in open('12.txt')]
mn = []
for i in l:
    if i % 3 == 0:
        mn.append(i)
mn = min(mn)
print(mn)
mx = []
for i in l:
    if str(i)[-1] == '3':
        mx.append(i)
mx = max(mx)
o = 0
c = []
for x in range(len(l) - 1):
    k = 0
    #if (mn <= l[x] <= mx and not(mn <= l[x + 1] <= mx)) or (not(mn <= l[x] <= mx) and mn <= l[x + 1] <= mx):
    if mn <= l[x] <= mx:
        k += 1
    if mn <= l[x + 1] <= mx:
        k += 1
    if k == 1:
        o += 1
        c.append(l[x] ** 2 + l[x + 1] ** 2)
print(o, min(c))