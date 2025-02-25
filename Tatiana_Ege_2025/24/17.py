s = open(r'C:\Users\Zarif\Downloads\403_1 (3).txt').readline()
s = s.replace('XX', '1')
s = s.replace('YY', '2')
s = s.replace('ZZ', '3')
mx = 1
ct = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1] and s[x] in '123' and s[x + 1] in '123':
        ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx * 2)