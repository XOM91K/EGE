import re
s = open(r'C:\Users\Zarif\Downloads\1087_1 (3).txt').readline()
m = re.findall(r'(?:LMN|MN|N)?(?:KLMN)+(?:KLM|KL|K)?', s)
print(len(max(m, key = len)))