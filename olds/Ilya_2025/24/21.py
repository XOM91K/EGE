import re
s = open('21.txt').readline()
m = re.findall(r"(?:[AOIUYE][^AOIUYE])+[AOIUYE]?", s)
print(len(max(m, key=len)))