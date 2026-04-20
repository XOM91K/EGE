import re
s = open(r'C:\Users\Zarif\Downloads\24_28943 (1).txt').readline()
s = s.split('20')
mn_ln = []
for x in range(len(s) - 24 - 1):
    ln = 0
    for y in range(0, 25):
        ln += len(s[x + y])
    if s[x + 25] != '' and s[x + 25][0] in 'AEOIUY':
        ln += 1
        mn_ln.append(ln)
print(min(mn_ln) + 2 * 26)
# s = s.replace('20', '#')
# m = re.findall(r'(?:#[^AEOIUY#]*){25}#[AEOIUY]', s)
# print(len((min(m, key=len))) + 26)