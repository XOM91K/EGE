s = open(r'C:\Users\Zarif\Downloads\24-263.txt').readline()
s = s.split('Y')
#Определите максимальную длину подстроки,
# в которой символ Y встречается не более 150 раз.
mx = 0
for x in range(len(s) - 150):
    sm = 0
    for y in range(151):
        sm += len(s[x + y])
    mx = max(mx, sm)
print(mx + 150)