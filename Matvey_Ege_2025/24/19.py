import re
s = open(r'C:\Users\Zarif\Downloads\1127_1 (1).txt').readline()
m = re.findall(r'AFD(?:(?:[1-9]\d+|0)[+*])+(?:[1-9]\d+|0)', s)
print(len(max(m, key=len)))
# (?:ABC)+   => ABCABCABCABCABCABC
# (ABC)+     => ABC