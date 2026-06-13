import re
s = open(r'C:\Users\Zarif\Desktop\24var08.txt').readline()
m = re.findall(r'(?=((?:(?:[1-9A-F][0-9A-F]*|0)[*-])+(?:[1-9A-F][0-9A-F]*|0)))', s)
print(max(m, key=len)) #\
print(len(max(m, key=len)))