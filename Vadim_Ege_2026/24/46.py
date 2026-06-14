import re
l = open(r'C:\Users\Zarif\Downloads\24 (35).txt').readline().replace('20','#')
m = re.findall(r'(?=((?:#[^AEIOUY#]*){25}#[^AEIOUY#]*[AEUIYO]))',l)
print(len(min(m,key=len)) + 26)