import re
a = open(r'C:\Users\Zarif\Downloads\1087_1.txt').readline()
m= re.findall(r'(?:LMN|MN|N)?(?:KLMN)+(?:KLM|KL|K)?',a)
maxx=  max(m, key=len)
print(len(maxx))