#
import re
a= open(r'C:\Users\Zarif\Downloads\1124_1 (1).txt').readline()
m = re.findall(r'(?:(?:[1-9]\d*[05]|0)[+*])+(?:[1-9]\d*[05]|0)?', a)
print(max(m, key=len))
print(len(max(m, key=len)))
# s = ''
# ct=0
# for i in range(len(a)):
#     for j in range(len(a)-i):
#         s=str(a[i:j])
#         try:
#             if eval(s)%5==0 and '*-' not in s and '*+' not in s:
#                 ct = max(ct , len(s))
#         except:
#             break
# print(ct)