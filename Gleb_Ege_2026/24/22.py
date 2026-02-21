import re
s = open(r'C:\Users\Zarif\Downloads\1397_2 (13).txt').readline()
s = s.replace('RSQ', '#')
s = re.findall(r'(?:#\w*?){129}#[^Q]+?', s)
print(len(min(s, key=len)) + 2 * 130)
# s = s.split('RSQ')
# mn_ln = []
# for x in range(len(s) - 128):
#     ln = 0
#     for y in range(0, 129):
#         ln += len(s[x + y])
#     mn_ln.append(ln + 130 * 3 + 1)
# print(min(mn_ln))