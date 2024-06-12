import re, string
print(string.ascii_uppercase)
s = open(r'C:\Users\Zarif\Downloads\24_623_1 (1).txt').readline()
m = re.findall(r"1[AEIOUY]+1|3[AEIOUY]+3|5[AEIOUY]+5|7[AEIOUY]+7|9[AEIOUY]+9", s)
print(len(max(m, key=len)))
print(max(m, key=len))