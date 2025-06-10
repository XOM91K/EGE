s = open(r'C:\Users\Zarif\Downloads\403_1 (2).txt').readline()
s = s.replace('XX', 'x')
s = s.replace('YY', 'y')
s = s.replace('ZZ', 'z')
st = ''
mx_ln = ''
for x in range(len(s) - 1):
    if s[x] != s[x + 1] and s[x] in 'xyz' and s[x + 1] in 'xyz':
        st += s[x]
    else:
        st += s[x]
        if len(st) > len(mx_ln):
            mx_ln = st
        st = ''
print(mx_ln)
mx_ln = mx_ln.replace('x', 'XX')
mx_ln = mx_ln.replace('y', 'YY')
mx_ln = mx_ln.replace('z', 'ZZ')
print(mx_ln)
print(len(mx_ln))