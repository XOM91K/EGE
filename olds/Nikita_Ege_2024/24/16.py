s = open('16.txt').readline().replace('C', 'B').split('B')
mn = 10 ** 10
for x in range(len(s) - 125):
    ct = 0
    for y in range(x, x + 126):
        ct += len(s[y])
    mn = min(mn, ct)
print(mn + 127)