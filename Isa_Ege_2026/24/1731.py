import re
s = open(r'C:\Users\Zarif\Downloads\1731_1 (4).txt').readline()
s = s.replace('02', '#')
m = re.findall(r'(?=((?:[^#AEOIUY]*#){20}[^#AEOIUY]*[AEOIUY]))', s)
print(len(max(m, key=len)) + 20)
#   asd#sa#
#02asdasd#asdasd#