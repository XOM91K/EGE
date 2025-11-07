import string
s = open(r'C:\Users\Zarif\Downloads\196_1 (9).txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x + x, x + ' ' + x)
s = s.split()
print(len(max(s, key=len)))
# s = ['Никита', 'Ян', 'Мирослав']
# print(max(s, key=len))
# ct = 0
# mx = []
# for x in range(len(s) - 1):
#     if s[x] != s[x + 1]:
#         ct += 1
#     else:
#         mx.append(ct + 1)
#         ct = 0
# print(max(mx))