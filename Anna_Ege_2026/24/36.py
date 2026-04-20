import re
s = open(r'C:\Users\Zarif\Downloads\24_28943 (2).txt').readline()
s = s.replace('20', '#')
m = re.findall(r'[AEOIUY](?:[^AEOIUY#]*#){26}[^AEOIUY#]*', s)
print(len(max(m, key=len)) + 26)
