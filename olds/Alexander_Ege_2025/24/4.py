import re
s = open(r'C:\Users\Zarif\Downloads\732_1.txt').readline()
m = re.findall(r'[A-WZ]+Y[A-WZ]+X[A-WZ]+|[A-WZ]+X[A-WZ]+Y[A-WZ]+', s)
print(len(max(m, key=len)))
# ASUIDGASIDUASGDSIUDGSDIUGIUXASIUDGASIUDGSIYIASHIDAUSGDI