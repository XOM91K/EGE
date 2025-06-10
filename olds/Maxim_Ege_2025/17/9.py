l = [int(x) for x in open('9.txt')]
k = 0
su = []
ma3 = []
ma32 = []
for x in l:
    if x % 3 == 0:
        ma3.append(x)
for x in l:
    if str(x)[-1] == '3':
        ma32.append(x)
min3 = min(ma3)
max3 = max(ma32)
for x in range(len(l)-1):
        sf = 0
        if l[x] >= min3 and l[x] <= max3:
            sf += 1
        if l[x+1] >= min3 and l[x+1] <= max3:
            sf += 1
        if sf == 1:
            k += 1
            su.append((l[x]**2 + l[x + 1]**2))
print(k,min(su))