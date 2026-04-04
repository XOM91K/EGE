import re
s = open('24.txt').readline()
m = re.findall(r'(?:T[^TAEOIUY]*){62}T[AEOIUY]', s)
print(len(min(m, key=len)))