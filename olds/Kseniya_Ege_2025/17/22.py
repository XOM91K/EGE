l = [int(x) for x in open('22.txt')]
mn = min(l)
mx = []
for x in range(len(l) -  1):
    if l[x] % 16 == mn or l[x + 1] % 16 == mn:
       mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))