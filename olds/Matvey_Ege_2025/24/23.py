s = open(r'C:\Users\Zarif\Downloads\403_1 (6).txt').readline()
s = s.replace('XX', '1').replace('YY', '2').replace('ZZ', '3')
ct = 1
mx_ln = 0
for x in range(len(s) - 1):
    if s[x] != s[x + 1] and s[x] in '123' and s[x + 1] in '123':
        ct += 1
        mx_ln = max(mx_ln, ct * 2)
    else:
        ct = 1
print(mx_ln)