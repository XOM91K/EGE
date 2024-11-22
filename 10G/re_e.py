import re
text = 'abc-def ghi-jk'
matches = re.findall(r'(\w+)-\w{2}', text)
print(matches)
