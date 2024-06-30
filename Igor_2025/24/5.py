import re, collections
s = open('5.txt').readline()
m = re.findall('X(\w)P', s)
print(collections.Counter(m).most_common()[0])
