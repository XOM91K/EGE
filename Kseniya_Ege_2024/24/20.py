s=open('20.txt').readline()
s=s.split('RO')
mx = 0
for x in range(len(s) - 21):
    ct = 0
    for y in range(x, x + 22):
        if s[y] != '' and (s[y][-1] == 'O' or s[y][0] == 'R'):
            break
        ct += len(s[y])
    else:
        mx = max(mx, ct + 42)
print(mx)