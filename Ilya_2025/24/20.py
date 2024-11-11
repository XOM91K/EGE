import re
a=open('20.txt').readline().replace('AXMM','$')
print(a)
s = re.findall(r'\w+', a)
print(s)
print(max(s, key = len))
print(len(max(s, key = len))+6)