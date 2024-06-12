import re
l = open('4.txt').readline()
m = re.findall('\.[A-Z]*?\.[A-Z]*?\.[A-Z]*?\.[A-Z]*?\.[A-Z]*?\.[A-Z]*?\.', l)
print(min(m, key = len), len(min(m, key=len)))