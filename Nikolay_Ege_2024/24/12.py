s = open('12.txt').readline()
ct = 1
mx_ct = 0
for x in range(len(s) - 1):
    if ord(s[x]) <= ord(s[x + 1]):
        ct += 1
        mx_ct = max(mx_ct, ct)
        if mx_ct == 10:
            print(x)
            break
    else:
        ct = 1
print(mx_ct)