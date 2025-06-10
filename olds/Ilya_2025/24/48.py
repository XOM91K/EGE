import re
s = open(r'C:\Users\Zarif\Downloads\24_19149.txt').readline()
m = re.findall(r'\(((?:\d+\+)+\d+)\)', s)
mx = 0
for x in m:
    if eval(x) % 2 == 0:
        mx = max(mx, len(x) + 2)
print(mx)