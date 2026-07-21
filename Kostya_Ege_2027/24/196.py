s = open(r'C:\Users\Zarif\Downloads\196_1 (16).txt').readline()
ct = 1
mx_ct = []
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
        mx_ct.append(ct)
    else:
        ct = 1
print(max(mx_ct))