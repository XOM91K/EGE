import re
s = open(r'C:\Users\Zarif\Downloads\1437_1 (3).txt').readline()
# m = re.findall(r'0[^Z]*Z?[^Z]*Z?[^Z]*Z?[^Z]*Z?[^Z]*0', s)
# print(max(m, key=len))
# print(len(max(m, key=len)))
s = s.split('Z')
mx_ln = []
for x in range(4, len(s)):
    ind = s[x].rfind('0')
    ln = 0
    if ind != -1:
        i = x
        ln += len(s[x])
        for y in range(4):
            i -= 1
            ind2 = s[i].find('0')
            if ind2 == -1:
                ln += len(s[i])
            else:
                ln += len(s[i][ind2 + 1:])
                break
    mx_ln.append(ln)
print(max(mx_ln) + 4)

# print(s)
# print(len(s))
# d = '12301230'
# print(d.rfind('0'))