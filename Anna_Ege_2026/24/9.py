import re
l = open(r'C:\Users\Zarif\Downloads\986_1 (3).txt').readline()
# [согл][любая буква][гласная]
m = re.findall(r'(?:[CDF]\w[AO])+', l)
print(len(max(m, key=len)) / 3)