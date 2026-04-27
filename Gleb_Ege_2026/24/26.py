import re
s = open('26.txt').readline()
m = re.findall(r'(?:\((?:[1-9]\d*[02468]|2|4|6|8)[+-](?:[1-9]\d*[13579]|1|3|5|7|9)\))+', s)
print(len(max(m, key=len)))