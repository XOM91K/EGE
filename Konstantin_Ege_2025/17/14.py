l=[int(x) for x in open('14.txt')]
ct=0
mx = 0
min_1 = min([x for x in l if x % 52 == 0])
for x in range(len(l)-2):
    if l[x] % 113 + l[x+1] % 113 + l[x+2] % 113 == min_1:
        ct += 1
        mx = max(mx, l[x] + l[x+1] + l[x + 2])
print(ct)
print(mx)