import re
a = open('33.txt').readline()
# s = re.findall(r'(?:\w*\.){5}\w+',a)
# print(len(max(s, key=len)))
s = a.split('.')
maxx= 0
strok=''
for i in range(len(s) - 5):
    maxx = max(maxx, len(s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] + s[i + 5]))
print(maxx + 5)
# SDAASD.ADDSDSA.ASDASDSDASD>DASDASD.ASDASDSD>ASDASD.ASDASD.