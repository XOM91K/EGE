import re
s = open(r'C:\Users\Zarif\Downloads\24_25361 (3).txt').readline()
m = re.findall(r'[02468](?:[^02468F]*F){76}[^02468F]*', s)
print(len(max(m, key=len)))
