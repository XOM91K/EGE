import re
s = open(r'C:\Users\Zarif\Downloads\EGE_24_29063 (1).txt').readline()
s = s.replace('20', '#')
m = re.findall('[AEOIUY](?:[^#AEOIUY]*#){26}[^#AEOIUY]*', s)
print((max(m, key=len)))
print(len(max(m, key=len)) + 26)