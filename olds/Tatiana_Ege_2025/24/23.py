s = open(r'C:\Users\Zarif\Desktop\ЕГКР\1 Вар\24.txt').readline()
s = s.split('QFG')
mn_ln = 10 ** 10
for x in range(len(s) - 105):
    ln = 0
    for y in range(1, 106):
        ln += len(s[x + y])
    for y in s[0][::-1]:
        if y == 'Q':
            ln += 1
        else:
            ln += 1
            break
    else:
        ln += 1
    mn_ln = min(mn_ln, ln + 3 * 105)
print(mn_ln)
# s = s.replace('QFG', '@')
# lns = []
# mn_ct = 10 ** 10
# ct = 0
# ind1 = [] # @
# last_Q = 0
# ind2 = [] # Q
# for x in range(len(s)):
#     if s[x] != '@':
#         if s[x] == 'Q':
#             ind2.append(x)
#
#         ct += 1
#     else:
#         ind1.append(x)
#         lns.append(ct)
#         if len(lns) == 104:
#             mn_ct = sum(lns) + 105 * 3
#         elif len(lns) > 104:
#             if ind1[-105]
#             mn_ct = min(mn_ct, mn_ct - lns[-106] + lns[-1] + 105 * 3)
#
#         ct = 0
# print(s)
# #RRRRRR@RRRRQRQ@RR@RR@RRRRRRRRRRRRRRR@
# # @ ind1 = [0, 6, 11, 15, 35]
# # Q ind2 = [8, 10]
# # @ три штуки
# # [6, 7, 2, 2
# # 12 - 6 + 2 = 8
# # 8 - 6 + 2 = 4