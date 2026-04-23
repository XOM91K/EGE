import re
t=open(r'C:\Users\Zarif\Downloads\1697_1 (2).txt').readline()
m=re.findall(r'(?:\((?:[1-9][0-9]*[02468]|0|2|4|6|8)[+-](?:[1-9][0-9]*[13579]|0|1|3|5|7|9)\))+', t)
print(len(max(m, key=len)))
print((max(m, key=len)))