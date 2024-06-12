s = open('33.txt').readline().split('Y')
mx_ln = 0
for x in s:
    if x.count('.') >= 5:
        d = x.split('.')
        for y in range(len(d) - 5):
            mx_ln = max(mx_ln, len(d[y] + d[y + 1] + d[y + 2] + d[y + 3] + d[y + 4] + d[y + 5]) + 5)
    else:
        mx_ln = max(mx_ln, len(x))
print(mx_ln)