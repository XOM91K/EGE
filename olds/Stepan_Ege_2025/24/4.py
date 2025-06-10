import re
s = open(r'C:\Users\Zarif\Downloads\24 (27).txt').readline()
m = re.findall(r'(?:[CDF][CDF][AO])+', s)
print(len(max(m, key=len)) / 3)