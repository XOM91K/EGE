l = open('17.txt').readlines()
ct = 0
mx = 0
for x in range(len(l)):
    l[x] = int(l[x])
print(l)
for x in range(len(l) - 1):
    if (l[x] % 3 == 0 or l[x + 1] % 3 == 0) and ((l[x] + l[x + 1]) % 5 == 0):
        ct += 1
        mx = max(l[x] + l[x + 1], mx)
print(ct, mx)