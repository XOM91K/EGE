import re
l = open(r'C:\Users\Zarif\Downloads\195_1 (7).txt').readline()
m = re.findall(r'2[KNLF]+2|0[KNLF]+0|4[KNLF]+4|6[KNLF]+6|8[KNLF]+8',l)
print(len(max(m,key=len)))