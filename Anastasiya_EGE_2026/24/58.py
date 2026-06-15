import re, itertools
s = open(r'C:\Users\Zarif\Downloads\24 (38).txt').readline()
mx = 0
for x in itertools.permutations('0123456789', 3):
    x = ''.join(x)
    shablon = f'[{x}]+'
    m = re.findall(rf'{shablon}', s)
    mx = max(mx, len(max(m, key=len)))
    print(mx)
# m = re.findall(r'\d+', s)
# mx = []
# for x in m:
#     if len(set(x)) == 3:
#         mx.append(x)
# print(len(max(mx, key=len)))
# print(m)