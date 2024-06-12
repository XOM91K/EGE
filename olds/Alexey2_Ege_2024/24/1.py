s = open('1.txt').readline()
ct = 1
mx_ct = 0
for x in range(len(s) - 1):
    if not((s[x].isalpha() and s[x + 1].isalpha()) or (s[x].isdigit() and s[x + 1].isdigit())):
        ct += 1
    else:
        mx_ct = max(mx_ct, ct)
        ct = 1
print(mx_ct)