s = open('19.txt').readline().split('++')
mx_len = 0
print(s)
for x in range(len(s) - 2):
    if s[x] != '' and s[x + 1] != '':
        d = s[x].split('+')
        d2 = s[x + 1].split('+')
        can = True
        for y in d:
            if len(y) > 0 and int(y) == 0:
                can = False
        for y in d2:
            if len(y) > 0 and int(y) == 0:
                can = False
        if can:
            mx_len = max(mx_len, len(s[x] + s[x + 1]) + 1)

print(mx_len)