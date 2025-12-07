import re
r = open(r"C:\Users\Zarif\Downloads\1171_1 (2).txt").readline()
m = re.findall(r'(?:(?:[12349][012349]*|0)[-*])+(?:[12349][012349]*|0)',r)
print(max(m,key=len))
print(len(max(m,key=len)))