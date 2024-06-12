s = open('1.txt').readline()
s = s.split('T')
mx_ln = 0
for i in range(len(s) - 100):
    ln = 0
    for j in range(101):
        ln += len(s[i + j])
    mx_ln = max(mx_ln, ln + 100)
print(mx_ln)