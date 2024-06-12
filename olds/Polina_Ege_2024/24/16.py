import re
s = open('16.txt').readline()
m = re.findall(r'[A-W](?:[A-W]*[XYZ]){15}[A-W]*', s)
mx = 0
for x in m:
    if x.count('X') == 5 and x.count('Y') == 5 and x.count('Z') == 5:
        mx = max(mx, len(x))
print(mx)