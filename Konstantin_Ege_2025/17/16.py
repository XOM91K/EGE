l=[int(x) for x in open('16.txt')]
ct=0
mx = 0
mn_ch =min([x for x in l if x > 0 and x % 10 == 4])
print(mn_ch)
for x in range(len(l) - 2):
    if sum(map(int, str(abs(l[x])))) + sum(map(int, str(abs(l[x + 1])))) + sum(map(int,str(abs(l[x + 2])))) == mn_ch:
            ct += 1
            mx = max(mx, l[x] + l[x + 1] + l[x + 2])
print(ct)
print(mx)