import re
s = open(r"C:\Users\Zarif\Downloads\1172_1 (6).txt").readline()
m = re.findall(r'(?:[1-9][0-9]*[+*])+[1-9][0-9]*',s)
mx = 0
# for x in m:
#     mx = max(mx, x.count('+') + x.count('*') + 1)
# print(mx)
k = max(m, key=lambda s1: s1.count('+') + s1.count('*'))
print(k)
n = k.count("+")+1+k.count('*')
print(n)