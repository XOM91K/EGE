import string
print(string.ascii_uppercase)
s = open(r'C:\Users\Zarif\Downloads\24_14510.txt').readline()
print(len(s))
for x in 'AIOUYE':
    s = s.replace(x, '#')
for x in 'BCDFGHJKLMNPQRSTVWXZ':
    s = s.replace(x, '$')
s = s.split('$$#')
mn_ln = 10 ** 10
for x in range(len(s) - 498):
    ln = 0
    for y in range(499):
        ln += len(s[x + y])
    mn_ln = min(mn_ln, ln + 500 * 3)
print(mn_ln)
# $$#
# mn_ln = 10**10
# d = 1
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i:j].count('$$#') == 500:
#             mn_ln = min(mn_ln, j - i)
#         if s[i:j].count('$$#') == 501:
#             break
#
# print(mn_ln)