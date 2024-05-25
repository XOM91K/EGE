s = open('2.txt').readline()
s = s.replace('XX', '1')
s = s.replace('YY', '2')
s = s.replace('ZZ', '3')
mx_ln = 0
ln = 0
print(s)
for x in range(len(s) - 1):
    if s[x].isalpha():
        ln = 1
    else:
        if len(set(s[x] + s[x + 1])) == 2:
            ln += 1
            mx_ln = max(mx_ln, ln)
        else:
            ln = 0
print(mx_ln * 2)