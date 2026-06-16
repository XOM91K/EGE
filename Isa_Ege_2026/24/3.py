import re
s = open(r'C:\Users\Zarif\Documents\24var02.txt').readline()
m = re.findall(r'L(?:[^L02468]*[02468]){14}[^L02468]*', s)
print(len(max(m, key=len)))