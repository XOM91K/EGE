import re
s = open(r'C:\Users\Zarif\Downloads\24_612_1 (2).txt').readline()
m = re.findall(r"(?:AB)+A?", s)
#Объединяющие сохраняющие и не сохраняющие скобки
print(len(max(m, key=len)))