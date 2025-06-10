import re
s = open(r'C:\Users\Zarif\Desktop\24-241 (1).txt').readline()
m = re.findall(r'O(?:(?:[A-E]*F?){2}[A-E]*O)+', s)
print(len(max(m, key=len)))
print(max(m, key=len))
# s = s.split('O')
# mx = 0
# ln = 0
# zap = 0
# for x in range(len(s)):
#     if s[x].count('F') <= 2:
#         zap += 1
#         ln += len(s[x])
#     else:
#         mx = max(mx, ln + zap + 1)
#         ln = 0
#         zap = 0
# print(mx)