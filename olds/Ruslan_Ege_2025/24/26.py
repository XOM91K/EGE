from re import *
s = open(r'C:\Users\Zarif\Downloads\1127_1 (5).txt').readline()
m = findall(r'AFD(?:(?:[1-9]\d*|0)[+*])+(?:[1-9]\d*|0)', s)
print(max(m, key=len))
print(len(max(m, key=len)))