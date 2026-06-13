import re
s = open(r'C:\Users\Zarif\Desktop\24var03.txt').readline()
s = s.split('1')
mx_ln = []
for x in range(len(s) - 700):
    ln = 0
    ct_CAT = 0
    for y in range(0, 701):
        ln += len(s[x + y])
        ct_CAT += s[x + y].count('CAT')

    last_str = s[x + 700]
    if 'CAT' in last_str:
        ln -= len(last_str) - (last_str.rindex('CAT') + 3)
    if ct_CAT >= 4:
        mx_ln.append(ln)
print(max(mx_ln) + 700)
# m = re.findall(r'(?:[^1]*1){700}[^1]*CAT', s)
# print(m)