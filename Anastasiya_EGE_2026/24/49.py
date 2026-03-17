s = open(r'C:\Users\Zarif\Downloads\24_27634.txt').readline()
s = s.split('Z')
mn = []
for x in range(len(s) - 268):
    ln = 0
    for y in range(269):
        ln += len(s[x + y])
    mn.append(ln + 270)
print(min(mn))