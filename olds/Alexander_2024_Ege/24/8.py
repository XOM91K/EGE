import re
s = open(r'C:\Users\Zarif\Downloads\24_9845.txt').readline()
m = re.findall(r"(?:[89][ABC])+|(?:[ABC][89])+", s)
print(len(max(m, key=len)))