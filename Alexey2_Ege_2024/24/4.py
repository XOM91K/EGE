s = open('4.txt').readline().split('@$@')
mx = 0
for x in range(len(s) - 2):
    mx = max(mx, len(s[x]) + len(s[x+1]) + len(s[x+2]) + 6)
print(mx)