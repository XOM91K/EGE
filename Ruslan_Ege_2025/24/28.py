import re
s = open(r'C:\Users\Zarif\Downloads\24.23_19887.txt').readline()
for x in '02468':
    s = s.replace(x, '0')
for x in '13579':
    s = s.replace(x, '1')
mx_ln = 0
ln = 1
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ln += 1
        mx_ln = max(mx_ln, ln)
    else:
        ln = 1
print(mx_ln)
# m = re.findall(r'(?:[02468][13579])+[02468]?|(?:[^02468][^13579])+[^02468]?', s)
# print(len(max(m, key=len)))