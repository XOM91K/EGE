import re
s = open(r'C:\Users\Zarif\Downloads\1090_1.txt').readline()
#s = open('10.txt').readline()
# m = re.findall(r'(?:\w*\.){5}\w*', s)
# print(len(max(m, key=len)))
s = s.split('.')
mx_ln = 0
for x in range(len(s) - 6):
    mx_ln = max(mx_ln, len(s[x] + s[x + 1] + s[x + 2] + s[x + 3] + s[x + 4] + s[x + 5]))
print(mx_ln + 5)