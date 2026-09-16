#
import re
s = open('/Users/zarif/Downloads/390_1.txt').readline()
m = re.findall(r'[^EYUIOA]?(?:[EYUIOA][^EYUIOA])+[EYUIOA]?',s)
print(len(max(m,key=len)))