import re, string
print(string.ascii_uppercase)
s = open('2.txt').readline()
for x in 'AIUYEO':
    s = s.replace(x, '#')
for x in 'BCDFGHJKLMNPQRSTVWXZ':
    s = s.replace(x, '@')
s = s.replace('##@', '%')
print(s)
# m = re.findall(r'(?:[AEOIUY][AEOIUY][^AEOIUY])+', s)
# print(len(max(m, key=len)) // 3)
# l = ['Никита', 'Владислав', 'Ян']
# print(max(l, key=len))