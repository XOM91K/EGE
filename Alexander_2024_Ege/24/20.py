sl = {}
s = open('20.txt').readline()
# import re
# m = re.findall('\w*0\w*1\w*2\w*3\w*4\w*5\w*6\w*7\w*8\w*9\w*A\w*B\w*C\w*D\w*E\w*F', s)
# print(max(m, key=len))
for x in '0123456789ABCDEF':
    sl[x] = []
j = 0
for x in range(len(s)):
    if s[x] in '0123456789ABCDEF':
        sl[s[x]].append(j)
        j = x + 1
j = min(sl['0'])
for x in sl:
    if sl[x] != '0':
        sl[x] = sorted(sl[x])
        for y in sl[x]:
            if y >= j:
                j = y
                break
print(min(sl['0']), j, max(sl['F']))