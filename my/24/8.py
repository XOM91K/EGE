import re
s = open(r'C:\Users\Zarif\Downloads\24_28765.txt').readline()
s = s.split('BC')
mx_ln = []
for x in range(len(s) - 180):
    ln = 0
    for y in range(181):
        ln += len(s[x + y])
    mx_ln.append(ln)
print(max(mx_ln) + 180 * 2 + 2)
# s = s.replace('BC', '#') #36166
# m = re.findall(r'(?:[^#]*#){180}[^#]*', s)
# print(max(m, key=len))
# print(len(max(m, key=len)) + 180)