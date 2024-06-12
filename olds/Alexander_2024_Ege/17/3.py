l = [int(x) for x in open('3.txt')]
ct = 0
mx = 0
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        if (l[x] + l[y]) % 10 == 0:
            ct += 1
            mx = max(mx, l[x] + l[y])
print(ct, mx)
