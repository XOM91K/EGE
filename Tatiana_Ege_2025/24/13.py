import re
s = open(r'C:\Users\Zarif\Downloads\986_1 (1).txt').readline()
m = re.findall(r'(?:[CDF]\w[AO])+', s)
print(max(m, key=len))
print(len(max(m, key=len)))