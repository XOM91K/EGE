s = open(r'C:\Users\Zarif\Downloads\24_10105 (1).txt').readline()
#s = open('3.txt').readline()
s = s.split('T')
mx_ln = 0
for x in range(len(s) - 100):
    ln = 0
    for y in range(0, 101):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln + 100)
print(mx_ln)