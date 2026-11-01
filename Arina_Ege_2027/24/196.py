#import re
s = open('/Users/zarif/Downloads/196_1.txt').readline()
mx_ct = []
ct = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ct += 1
        mx_ct.append(ct)
    else:
        ct = 1
print(max(mx_ct))

#m = re.findall(r'', s)