s = open('21.txt').readline()
s = s.split('Z')
mn = 1000000000
for x in range(len(s) - 118):
    ct = 0
    for y in range(x, x + 119):
        ct += len(s[y])
    mn = min(mn, ct + 120)
print(mn)