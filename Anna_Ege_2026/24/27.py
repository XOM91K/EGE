s = open(r'C:\Users\Zarif\Downloads\24_23762.txt').readline()
s = s.split('Y')
mx = []
for x in range(len(s) - 80):
    ln = 0
    ct2025 = 0
    for y in range(81):
        ln += len(s[x + y])
        ct2025 += s[x + y].count('2025')
    if ct2025 >= 90:
        mx.append(ln + 80)
print(max(mx))
# 24374 разобрать эту задачу
