s = open(r'C:\Users\Zarif\Desktop\ЕГКР\1 Вар\24.txt').readline().split('QFG')
mn_ln = 10 ** 10
for x in range(len(s) - 104):
    ln = 0
    for y in range(1, 105):
        ln += len(s[x + y])
    for y in s[x][::-1]:
        if y == 'Q':
            ln += 1
        else:
            ln += 1
            break
    else:
        ln += 1
    mn_ln = min(mn_ln, ln + 105 * 3)
print(mn_ln)