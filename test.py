import re
s = open(r'C:\Users\Zarif\Downloads\24_23206.txt').readline()
m = re.findall(r'[02468][13579A-Z]{291}', s)
for x in m:
    if x.count('S') == 35:
        print(len(x), x)