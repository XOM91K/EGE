s = open('9.txt').readline()
s = s.replace('E', 'D').replace('F', 'D').split('D')
mx_ct = 0
r = ['ABC', 'BAC', 'CAB', 'CBA']
for x in s:
    if x != '':
        ct = 0
        for y in range(0, len(x) - 2, 2):
            if x[y] + x[y + 1] + x[y + 2] in r:
                ct += 1
                mx_ct = max(mx_ct, ct)
            else:
                ct = 0
print(mx_ct)