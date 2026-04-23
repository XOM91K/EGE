# import re
# s = open(r'C:\Users\Zarif\Downloads\24_28943 (3).txt').readline()
# s = s.split('20')
# mnln = []
# for x in range(len(s) - 25):
#     ln = 0
#     for y in range(25):
#         if 'A' in s[x + y] or 'E' in s[x + y] or 'O' in s[x + y] or 'I' in s[x + y] or 'U' in s[x + y] or 'Y' in s[x + y]:
#             ln += 1000
#             break
#         ln += len(s[x + y])
#     last = s[x + 25]
#     if ln == 57:
#         print('ok')
#     for y in last:
#         if y not in 'AEOIUY':
#             ln += 1
#         else:
#             ln += 1
#             break
#     mnln.append(ln + 52)
# print(min(mnln))
# # s = s.replace('20', '#')
# # m = re.findall(r'(?:#[^AEOIUY#]*?){25}#[^AEOIUY#]*?[AEOIUY]', s)
# # print(len(min(m, key=len)) + 26)
