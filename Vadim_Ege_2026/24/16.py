import re
r = open(r"C:\Users\Zarif\Downloads\196_1 (14).txt").readline()
mx = 0
ct = 1
for x in range(len(r) - 1):
    if r[x] != r[x + 1]:
       ct += 1
    else:
        mx = max(mx, ct)
        ct = 1
print(mx)
# m = re.findall(r'[A-Z]+', r)
# #print(max(m,key=len))
# print(len(max(m,key=len)))