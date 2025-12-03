import re
s = open(r'C:\Users\Zarif\Downloads\24_23281.txt').readline()
s = s.split('Y')
mx = []
for x in range(len(s) - 80):
    c2025 = 0
    ln = 0
    for y in range(81):
        c2025 += s[x + y].count('2025')
        ln += len(s[x + y])
    if c2025 >= 90:
        mx.append([ln, c2025])
print(max(mx)) # + 80
# s = s.replace('2025', '#')
# рока 2025 встречается не менее 90 раз
# и при этом содержится ровно 80 букв Y.
#
# m = re.findall(r"(?:[^#Y]*#)*(?:[^#Y]*[#Y]){80}(?:[^#Y]*#)*", s)
# print(len(max(m, key=len)))
# print(max(m, key=len).count('#'))
# m = re.finditer(r"(?=((?:[^#Y]*[#Y])+[^#Y]*))", s)
# ln = 0
# # 324
# for x in m:
#     if x.group(1).count('Y') == 80 and x.group(1).count('#') >= 90:
#         print(x.group(1).count('#'), x.group(1))
#         break
#     #ln = max(ln, len(x.group(1)))
# #print(ln)
# # 324 + 209 * 3
# # 2981