import re
s = open(r'C:\Users\Zarif\Downloads\175_1 (10).txt').readline()
print(s)
# A, B, C, D, E, F, O
m = re.findall(r'(?:O(?:[^OF]*F){0,2}[^OF]*)+O', s)
print(m)
print(max(m, key=len))
print(len(max(m, key=len)))
# [^OF]*F[^OF]*F
# [^OF]*F[^OF]*
# O[^OF]*O
#O(?:[^OF]*F){0,2}[^OF]*O