import re
s = open(r'C:\Users\Zarif\Downloads\732_1 (1).txt').readline()
m = re.findall(r'[^XY]+Y[^XY]+X[^XY]+', s)
print(len(max(m, key=len)))
# l=l.replace('X', '@')
# l=l.replace('Y', ' ')
# l=l.split(' ')
# print(l)
# r = []
# for x in l:
#     if x.count('@') == 1:
#             r.append(len(x))
# print(max(r))