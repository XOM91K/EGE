s = open(r'C:\Users\Zarif\Downloads\24_12476.txt').readline()
s = s.split('RO')
mx = 0
for x in range(len(s) - 21):
    ct = 1
    st = ''
    for y in range(x, x + 22):
        if ((len(s[y]) > 0) and (s[y][-1] == 'O' or s[y][0] == 'R')) or (len(s[y]) == 0):
            ct = 1
            continue
        ct += len(s[y])
        st = s[y]
    mx = max(mx, ct + (21 * 2))
print(mx)
#ASDASDO,RO, RO, ASDASDSD