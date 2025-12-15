import re
s = open(r'C:\Users\Zarif\Downloads\24_25361.txt').readline()
for x in '02468':
    s = s.replace(x, '#')
m = re.findall('#(?:[^F#]*F){76}[^F#]*', s)
print(m)
print(len(max(m, key=len)))