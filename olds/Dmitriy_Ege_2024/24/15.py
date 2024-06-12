import re
s = open(r'C:\Users\Zarif\Downloads\24_624_1.txt').readline()
m = re.findall(r"8[KNLF]+8", s)
print(len(max(m, key=len))) #5105