import re
a = open(r'C:\Users\Zarif\Downloads\1088_1.txt').readline().replace('CD','#')
# s = re.findall(r'(?: \w*#){160}', a)
# print(s)
s = a.split('#')
print(s)
a=[]
for i in range(len(s) - 160):
    sum = 0
    for x in range(0, 161):
        sum += len(s[i+x])
    a.append(sum)
print(max(a) + 320 + 2)
#CDASDASDHASIODSHDASODSGDOASGDOIASGCD