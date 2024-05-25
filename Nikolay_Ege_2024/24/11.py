s = open('11.txt').readline()
ct = 1
mx_ct = 0
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
        mx_ct = max(mx_ct, ct)
    else:
        ct = 1
print(mx_ct)