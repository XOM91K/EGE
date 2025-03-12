import re
a = open(r'C:\Users\Zarif\Downloads\328_1 (3).txt').readline().split('CD')
mx_ln = 0
for x in range(len(a) - 50):
    ln = 0
    for y in range(51):
        ln += len(a[x + y])
    mx_ln = max(mx_ln, ln + 100)
print(mx_ln + 2)