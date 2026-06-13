import re
s = open(r'C:\Users\Zarif\Downloads\24 (34).txt').readline()
s = s.replace('BC', '#')
m = re.findall(r'(?=((?:[^#]*#){190}[^#]*))', s)
print(len(max(m, key=len)) + 190)
# s = open(r'C:\Users\Zarif\Downloads\24 (34).txt').readline()
# s = s.split('BC')
# mx_ln = []
# for x in range(len(s) - 190):
#     ln = 0
#     for y in range(0, 191):
#         ln += len(s[x + y])
#     mx_ln.append(ln + 190 * 2)
# print(max(mx_ln))