s = open('21.txt').readline()
#24 задача из Досрока
s = s.replace('A', '@')
s = s.replace('B', '@')
s = s.replace('C', '@')
s = s.replace('6', '#')
s = s.replace('7', '#')
s = s.replace('8', '#')
s = s.replace('9', '#')
s = s.replace('@@', '$')
s = s.replace('##', '$')
s = s.split('$')
# ct = 1
# mx = 0
# print(s)
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         ct += 1
#     else:
#         mx = max(mx, ct)
#         ct = 1
# print(mx)
print(max(s, key=len))
print(len(max(s, key=len)))
