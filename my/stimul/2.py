import re
s = open('2.txt', encoding='UTF-8').readline()
#print(s)
ss = re.findall("\(\d*,12,'ege'.*?\),", s)
for x in ss:
    print(x, end=' ')