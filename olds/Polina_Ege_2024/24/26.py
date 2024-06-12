s = open(r'C:\Users\Zarif\Downloads\24 (20).txt').readline()
mx_ln = 0
ct = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
        mx_ln = max(mx_ln, ct)
    else:
        mx_ln = max(mx_ln, ct)
        ct = 1
print(mx_ln)