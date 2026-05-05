import re
s = open(r'C:\Users\Zarif\Downloads\1731_1 (1).txt').readline()
s = s.replace('02','#')
m = re.findall(r'[^AEIOUY#]*(?:#[^AEIOUY#]*){20}[AEIOUY]', s)
print(len(max(m, key=len))+20 + 1)