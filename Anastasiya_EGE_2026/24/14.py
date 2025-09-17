#dz 2
import re
s = open(r'C:\Users\Zarif\Downloads\24_5677.txt').readline()
m = re.findall(r'(?:AD|D)(?:DAD)+(?:DA|D)', s)
print(len(max(m, key=len)))