import re
s = open('5.txt').readline()
m = re.findall(r"0[KNLF]+0|2[KNLF]+2|4[KNLF]+4|6[KNLF]+6|8[KNLF]+8", s)
print(len(max(m, key=len)))
s = [1,2,3]