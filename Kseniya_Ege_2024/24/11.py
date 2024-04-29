s = open('12.txt').readline().split('Z')
mx_ln = 10 ** 10
for x in range(len(s) - 118):
    ct = 0
    for y in range(x, x + 119):
        ct += len(s[y])
    mx_ln = min(mx_ln, ct)
print(mx_ln + 120)