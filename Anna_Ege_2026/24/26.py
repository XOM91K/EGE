import re
s = open(r'C:\Users\Zarif\Downloads\24_24895 (1).txt').readline()
# m = re.findall(r'(?:\d+[+*]){39}\d+', s)
# print(len(max(m, key=len)))
s = s.replace('+', '*').split('*')
mx = []
for x in range(len(s) - 39):
    ln = 0
    for y in range(40):
        ln += len(s[x + y])
        if '' == s[x + y]:
            ln = 0
            break
    mx.append(ln + 39)
print(max(mx))
