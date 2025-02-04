s = open(r'C:\Users\Zarif\Downloads\196_1 (5).txt').readline()
mx_ln = 0
ln = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ln += 1
        mx_ln = max(mx_ln, ln)
    else:
        ln = 1
print(s)
print(mx_ln)