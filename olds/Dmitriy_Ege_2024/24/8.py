import re
s = 'imgimgimgimg'
s = open(r'C:\Users\Zarif\Downloads\24_633_1.txt').readline()
m = re.findall(r'(?:[BCDFGHJKLMNPQRSTVWXZ][A-Z][AEIOUY])+', s)
print(max(m, key=len))
print(m)