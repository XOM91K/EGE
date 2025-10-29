import re
s = open(r'C:\Users\Zarif\Downloads\175_1 (13).txt').readline()
s = s.split('O')
mx = 0
ln = 0
for x in s:
    if x.count('F') <= 2:
        ln += len(x) + 1
    else:
        mx = max(mx, ln + 1)
        ln = 0
print(mx)
# m = re.findall(r'O(?:(?:[^O]*F){,2})+[^O]*O', s)
# print(len(max(m, key=len)))

# l = open('175_1.txt').readline()
# mx = -float('inf')
# l = l.split('O')
# print(l[:20])
# for x in l:
#     if x.count('F')<=2:
#         if len(x)+ 2 > mx:
#             mx = len(x) + 2
# print(mx)