s = open('12.txt').readline().replace('C','B').split('B')
mn_ln = 10 ** 10
for x in range(len(s) - 125):
    ct = 0
    for y in range(x, x + 126):
        ct += len(s[y])
    mn_ln = min(mn_ln, ct)
print(mn_ln + 127)