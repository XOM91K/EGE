s = open(r'C:\Users\Zarif\Desktop\ЕГКР\1 Вар\24.txt').readline()
d = s
s = s.split('QFG')
i = 0
j = 103
mn_ln = 10 ** 10
str_mn_ln = ''
while j != len(s):
    nash_str = 'QFG'.join(s[i: j + 1])
    if len(nash_str) < mn_ln:
        mn_ln = len(nash_str)
        str_mn_ln = nash_str
    i += 1
    j += 1
print(str_mn_ln)
print(d.find(str_mn_ln))
print(d[7086655:7086665])