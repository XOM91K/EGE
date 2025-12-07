import re
r = open(r"C:\Users\Zarif\Downloads\390_1 (9).txt").readline()
m = re.findall(r'(?:[AUYOIE][^AUYOIE])+[AUYOIE]?|(?:[^AUYOIE][AUYOIE])+[^AUYOIE]?',r)
print(len(max(m,key=len)))