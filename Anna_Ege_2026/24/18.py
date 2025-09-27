import re
s = open(r'C:\Users\Zarif\Downloads\24_17641 (1).txt').readline()
m = re.findall(r'(?:[1-9]\d*[*+])+[1-9]\d*', s)
for x in m:
    if eval(x) == 0:
        print(x)