import re
s = open('46.txt').readline()
m = re.findall(r'(?:T[^AEOIUYT]*?){62}T[^AEOIUYT]*?[AEOIUY]', s)
print(len(min(m, key=len)))