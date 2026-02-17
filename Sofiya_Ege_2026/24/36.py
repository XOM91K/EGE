import re
s = open(r'C:\Users\Zarif\Downloads\1397_2 (11).txt').readline()
# s = s.split('RSQ')
# mn_ln = 10 ** 10
# for x in range(len(s) - 128):
#     ln = 0
#     for y in range(0, 129):
#         ln += len(s[x + y])
#     mn_ln = min(mn_ln, ln + 3 * 130)
# print(mn_ln)
# s = s.replace('RSQ', '#')
# m = re.findall(r'(?:#\w*?){129}#[^Q]+?', s)
# print(len(min(m,key=len)) + 2 * 130)