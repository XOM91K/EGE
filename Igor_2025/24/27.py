import re
s = open(r'C:\Users\Zarif\Downloads\24_19751 (1).txt').readline()

# dd = '91027102udj'
# m = re.search('\d*', dd)
# print(m.group())
# exit()
for x in 'BCD-*':
    s = s.replace(x, '#')
s = s.split('A')
mx = 0
for x in s:
    m = re.search(r'\b(?:\d+\+)+\d+', x)
    if m is not None:
        if m.span()[0] == 0:
            mx = max(mx, sum(map(int, m.group().split('+'))))
print(mx)

# m = re.findall(r'A((?:[1-9]+\+)+[1-9]+)', s)
# print(eval(max(m, key=eval)))
# print(max(m, key=eval))
#67622777
#7288704
#7288704   7288697+1+6 7288704
#525375679