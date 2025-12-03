# import re
# s = open(r'C:\Users\Zarif\Downloads\1090_1 (6).txt').readline()
# m = re.finditer(r'(?=([A-Z]+(?:[A-Z]*\.){5}[A-Z]+))', s)
# mx_ln = 0
# for x in m:
#     mx_ln = max(mx_ln, len(x.group(1)))
# print(mx_ln)
s = open(r'C:\Users\Zarif\Downloads\1090_1 (6).txt').readline()
s = s.split('.')
mn_ln = []
for x in range(len(s) - 5):
    mn_ln.append(len(s[x] + s[x + 1] + s[x + 2] + s[x + 3] + s[x + 4] + s[x + 5]))
print(max(mn_ln) + 5)