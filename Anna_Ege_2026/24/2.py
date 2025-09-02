s = open(r'C:\Users\Zarif\Downloads\24_21.txt').readline()
s = s.replace('XX', 'X X')
s = s.replace('YY', 'Y Y')
s = s.replace('ZZ', 'Z Z')
s = s.split(' ')
print(len(max(s, key=len)) - 1)
# for x in range(len(s) - 1):
#     if s[x] != s[x + 1]:
#         ct += 1
#     else:
#         mx = max(mx, ct)
#         ct = 1
# print(mx)