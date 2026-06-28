import re

mx = []
t = open(r'C:\Users\Zarif\Downloads\24_29924.txt').readline()
m = re.findall(r'(?=((?:[02468ACE][13579BDF]*){259}[02468ACE]))',t)
for x in m:
    mx.append(x.lstrip('0'))
print(len(min(mx,key=len)))
# m = re.findall(r'(?=([0123456789ABCDEF]{260,}))', t)
# for x in m:
#     ct = 0
#     for a in x:
#         if a in '02468ACE':
#             ct += 1
#     if ct == 260:
#         mx.append(x.lstrip('0'))
# print(len(min(mx, key=len)))
# print((min(mx, key=len)))
