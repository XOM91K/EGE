import re
l = open(r'38.txt').readline()
m = re.findall(r'(?:\((?:[1-9][0-9]*[02468]|2|4|6|8)[-+](?:[1-9][0-9]*[13579]|1|3|5|7|9)\))*',l)
print(len(max(m,key=len)))