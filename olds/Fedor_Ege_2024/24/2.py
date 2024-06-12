s = open(r'2.txt').readline()
s = s.split('Y')
mx = 0
for x in range(len(s) - 150):
    ct = 0
    for y in range(x, x + 151):
        ct += len(s[y])
    mx = max(mx, ct)
print(mx + 150)