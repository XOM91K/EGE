s = open('9.txt').readline().split('Y')
mx_ln = 0
for x in range(len(s) - 150):
    ln = 0
    for y in range(151):
        ln += len(s[x + y])
    mx_ln = max(mx_ln, ln + 150)
print(mx_ln)