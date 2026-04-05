import re
s = open(r'C:\Users\Zarif\Downloads\1483_1 (13).txt').readline()
s = s.replace('CDE', '#')
m = re.findall('(?:#[^#]*?){86}#[^E#]+?', s)
print(len(min(m, key=len)) + 87 * 2)
# s = s.split('CDE')
# ln_mn = []
# for x in range(len(s) - 86):
#     ln = 0
#     for y in range(86):
#         ln += len(s[x + y])
#     for y in s[x + 86]:
#         ln += 1
#         if y != 'E':
#             break
#     ln_mn.append(ln + 3 * 87)
# print(min(ln_mn))
