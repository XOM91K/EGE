s = open('196_1 (4).txt').readline()
mx_ln = 1
ln = 1
#ABCDEE
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        ln += 1
        mx_ln = max(mx_ln, ln)
    else:
        ln = 1
print(mx_ln)