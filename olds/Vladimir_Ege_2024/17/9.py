l = [int(x) for x in open('10.txt')]
ct = 0
su = 0
for x in range(len(l) - 1):
    if (l[x] % 19 == 0 or l[x + 1] % 19 == 0):
        ct += 1
        su = max(su, l[x] + l[x + 1])
print(ct, su)