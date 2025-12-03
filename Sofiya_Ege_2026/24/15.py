import re
s = open(r'C:\Users\Zarif\Downloads\988_1 (5).txt').readline()
m = re.findall(r'(?:\.[A-Z]*){6}\.', s)
print(min(m, key=len))
print(len(min(m, key=len)))
# s = s.split('.')
# mx_ln = []
# for x in range(len(s) - 5):
#     mx_ln.append(len(s[x]) + len(s[x + 1]) + len(s[x + 2]) + len(s[x + 3]) + len(s[x + 4]) + len(s[x + 5]))
# print(min(mx_ln) + 7)