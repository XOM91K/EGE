import re
s = open(r'C:\Users\Zarif\Downloads\195_1 (11).txt').readline()
m = re.findall(r'0[KNLF]+0|2[KNLF]+2|4[KNLF]+4|6[KNLF]+6|8[KNLF]+8', s)
print(len(max(m, key=len)))