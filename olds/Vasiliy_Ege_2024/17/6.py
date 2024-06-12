l = [int(x) for x in open('6.txt')]
ct = 0
su = 0
mx = 0
for x in l:
    if x % 19 == 0:
        mx = max(mx, x)
print(mx)
for x in range(len(l) - 1):
    if l[x] > mx or l[x + 1] > mx:
        ct += 1
        su = max(su, l[x] + l[x + 1])
print(ct, su)