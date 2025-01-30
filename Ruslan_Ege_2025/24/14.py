import re
s = open(r'C:\Users\Zarif\Downloads\403_1.txt').readline()
s = s.replace('XX', 'A').replace('YY', 'B').replace('ZZ', 'C')
for x in 'TUVWXYZ':
    s = s.replace(x, '#')
s = s.split('#')
mx_ln = 0
for x in s:
    if len(x) >= 2:
        ln = 1
        for y in range(len(x) - 1):
            if x[y] != x[y + 1]:
                ln += 1
                mx_ln = max(mx_ln, ln)
            else:
                ln = 1
print(mx_ln * 2)
print(s)
#m = re.findall(r'(?:XX|ZZ|YY)+', s)
#print(len(max(m, key=len)))
#print(m)