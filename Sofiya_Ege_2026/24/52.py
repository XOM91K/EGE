import re
s = open(r'C:\Users\Zarif\Downloads\24_22356.txt').readline()
print('otvet:', s.index('9BB200831629754013654089270916572830406015947823017328604590726108439503251640897095740682310273940168500024B'))
m = re.findall(r'[1-9AB][0-9AB]+[13579B]', s)
ln = len(max(m, key=len))
print(max(m, key=len))
for x in m:
    if len(x) == ln:
        print(x)
# for c in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
#     s=s.replace(c, '#')
# for c in '13579AB':
#     s=s.replace(c, '!')
# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         c=s[l:r+1]
#         if '#' in c:
#             break
#         elif c[-1]=='!':
#             m=max(m, len(c))
#             d.append((l, c))
# print(max(d, key=lambda p: len(p[0])))
# print(max(d))
