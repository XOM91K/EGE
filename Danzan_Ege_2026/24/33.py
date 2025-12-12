import re
s = open(r'C:\Users\Zarif\Downloads\24 (5)_23424.txt').readline()
m = re.findall('A[^A-Z]+A|E[^A-Z]+E|I[^A-Z]+I|O[^A-Z]+O|U[^A-Z]+U|Y[^A-Z]+Y', s)
print(len(max(m, key=len)))