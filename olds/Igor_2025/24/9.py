import re
s = open('9.txt').readline()
m = re.findall('(?:LMN|MN|N)?(?:KLMN)+(?:KLM|KL|K)?', s)
print(len(max(m, key=len)))