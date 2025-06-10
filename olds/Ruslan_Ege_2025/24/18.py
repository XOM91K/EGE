import re
s = open(r'C:\Users\Zarif\Downloads\986_1.txt').readline()
m = re.findall(r'(?:[CDF]\w[AO])+', s)
print(len(max(m, key=len)))
print(max(m, key=len))