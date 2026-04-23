import re
s = open(r'C:\Users\Zarif\Downloads\EGE_24_29063.txt').readline()
s = s.replace('20', '#')
m = re.findall(r'[AEOIUY](?:[^AEOIUY#]*#){26}[^AEOIUY#]*', s)
print(len(max(m, key=len)) + 26)
print(max(m, key=len))