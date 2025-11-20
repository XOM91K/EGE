import re
t=open(r'C:\Users\Zarif\Downloads\327_1 (6).txt').readline()
m=re.findall('[A-Z](\d+[02468])[A-Z]', t)
print(max(m, key=int))
#F54476W
#F94476W